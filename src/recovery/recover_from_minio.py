import subprocess
from pathlib import Path
import polars as pl
from datetime import datetime

SOURCE = "minio/warehouse/bronze/bronze_jobs/data"

OUTPUT_DIR = Path("src/recovery/output")
OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


DOWNLOAD_DIR = Path("src/recovery/recovery_objects")
DOWNLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

OUTPUT_PARQUET = OUTPUT_DIR / f"recovery_{timestamp}.parquet"
OUTPUT_CSV = OUTPUT_DIR / f"recovery_{timestamp}.csv"



# ==========================================
# 1. LIST OBJECT FROM MINIO
# ==========================================

result = subprocess.run(
    [
        "docker",
        "exec",
        "minio",
        "bash",
        "-c",
        f"mc ls {SOURCE}"
    ],
    capture_output=True,
    text=True
)


objects = []


for line in result.stdout.splitlines():

    parts = line.split()

    if len(parts) < 5:
        continue


    size = parts[3]
    name = parts[5]


    if not name.endswith(".parquet"):
        continue


    if size == "0B":
        print("SKIP EMPTY:", name)
        continue


    objects.append(name)



print(
    "Objects found:",
    len(objects)
)



# ==========================================
# 2. DOWNLOAD + READ PARQUET
# ==========================================

dfs = []


for obj in objects:

    target = DOWNLOAD_DIR / obj


    print("\nDownloading:")
    print(obj)



    subprocess.run(
        [
            "docker",
            "exec",
            "minio",
            "mc",
            "cp",
            f"{SOURCE}/{obj}",
            f"/tmp/{obj}"
        ],
        check=True
    )



    subprocess.run(
        [
            "docker",
            "cp",
            f"minio:/tmp/{obj}",
            str(target)
        ],
        check=True
    )



    try:

        df = pl.read_parquet(target)


        print(
            "SUCCESS rows:",
            df.height
        )


        dfs.append(df)



    except Exception as e:

        print(
            "FAILED:",
            obj,
            e
        )




# ==========================================
# 3. MERGE
# ==========================================

print("\n====================")

print(
    "VALID FILES:",
    len(dfs)
)



if not dfs:

    raise Exception(
        "No data recovered"
    )



bronze = pl.concat(
    dfs,
    how="vertical"
)



print(
    "TOTAL BEFORE DEDUP:",
    bronze.height
)



# ==========================================
# 4. DEDUPLICATION
# ==========================================

bronze = bronze.unique(
    subset=["job_id"],
    keep="last"
)



print(
    "TOTAL AFTER DEDUP:",
    bronze.height
)



# ==========================================
# 5. SAVE RECOVERY OUTPUT
# ==========================================


bronze.write_parquet(
    OUTPUT_PARQUET
)



bronze.write_csv(
    OUTPUT_CSV
)



print("\n====================")

print("RECOVERY COMPLETE")

print(
    "PARQUET:",
    OUTPUT_PARQUET
)

print(
    "CSV:",
    OUTPUT_CSV
)