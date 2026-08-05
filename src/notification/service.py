from src.notification.rules import (
    should_notify,
    TARGET_ROLES,
    TARGET_SENIORITY,
)
from src.notification.formatter import format_job_notification
from src.notification.ntfy_client import send_notification



def send_job_notifications(jobs):

    if not jobs:

        print(
            "[INFO] No new jobs."
        )

        return


    total_jobs = len(jobs)

    matched_jobs = 0

    sent = 0


    for job in jobs:


        if not should_notify(job):

            continue


        matched_jobs += 1


        notification = format_job_notification(
            job
        )


        send_notification(
            title=notification["title"],
            message=notification["message"],
            priority="default",
            tags=[
                "briefcase"
            ],
        )


        sent += 1


    print(
        f"[INFO] Jobs received       : {total_jobs}"
    )

    print(
        f"[INFO] Roles Parameter: "
        f"{TARGET_ROLES}, "
        f"{TARGET_SENIORITY}"
    )
    
    print(
        f"[INFO] Rule matched jobs   : {matched_jobs}"
    )

    print(
        f"[INFO] Notifications sent : {sent}"
    )