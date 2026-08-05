from src.notification.service import send_job_notifications


if __name__ == "__main__":


    dummy_jobs = [

        {
            "title": "Data Engineer",
            "company": "Tokopedia",
            "posted_date_clean": "05 August 2026",
            "location": "Jakarta",
            "seniority_level": "Entry Level",
            "required_skills": [
                "Python",
                "SQL",
                "Airflow"
            ],
            "detail_url":
            "https://google.com"
        },


        {
            "title": "Frontend Developer",
            "company": "Company B",
            "posted_date_clean": "05 August 2026",
            "location": "Remote",
            "seniority_level": "Associate",
            "required_skills": [
                "React"
            ],
            "detail_url":
            "https://google.com"
        }

    ]


    send_job_notifications(
        dummy_jobs
    )