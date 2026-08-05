from src.pipeline.ingestion import run_ingestion

#UBAH KEYWORDS PENCARIAN
KEYWORDS = [
    "Junior Data Engineer",
    "Junior Data Scientist",
    "Machine Learning AI Engineer",
]

# UBAH JUMLAH DATA PER PENCARIAN
MAX_RESULTS = 10



def main():

    jobs = run_ingestion(
        keywords=KEYWORDS,
        max_results=MAX_RESULTS
    )


    print() 

    print("=" * 60)
    print(f"TOTAL JOBS : {len(jobs)}")
    print("=" * 60)



if __name__ == "__main__":

    main()