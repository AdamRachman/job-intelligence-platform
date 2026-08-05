def format_job_notification(job):

    title = job.get(
        "title",
        "-"
    )

    company = job.get(
        "company",
        "-"
    )

    posted_date = job.get(
        "posted_date_clean",
        "-"
    )

    location = job.get(
        "location",
        "-"
    )

    skills = job.get(
        "required_skills",
        []
    )


    if isinstance(skills, list):
        skills = ", ".join(skills)


    detail_url = job.get(
        "detail_url",
        "-"
    )


    message = f"""
Company: {company}
Date: {posted_date}
Location: {location}
Stack: {skills}

[Apply Job]({detail_url})
"""


    return {
        "title": title,
        "message": message.strip()
    }