from trino.dbapi import connect


# Trino configuration
TRINO_HOST = "localhost"
TRINO_PORT = 8080
TRINO_USER = "admin"


def test_trino_connection():

    try:
        conn = connect(
            host=TRINO_HOST,
            port=TRINO_PORT,
            user=TRINO_USER,
            catalog="iceberg",
            schema="gold"
        )

        cursor = conn.cursor()

        print("[PASS] Trino connection success")


        query = """
        SELECT
            source,
            job_id,
            title,
            company,
            location,
            employment_type,
            seniority_level,
            required_skills,
            detail_url,
            scraped_at
        FROM iceberg.gold.gold_jobs
        LIMIT 5
        """


        cursor.execute(query)

        rows = cursor.fetchall()

        print(f"[PASS] Query success. Rows returned: {len(rows)}")


        for row in rows:
            print("-" * 50)
            print(row)


        cursor.close()
        conn.close()


    except Exception as e:
        print("[FAILED]")
        print(type(e))
        print(repr(e))


if __name__ == "__main__":
    test_trino_connection()