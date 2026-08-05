from src.notification.ntfy_client import send_notification


if __name__ == "__main__":

    send_notification(
        title="Data Engineer Test",
        message="""
Company:
Test Company

Location:
Jakarta

Stack:
Python, SQL

[Apply Job](https://google.com)
        """,
        priority="default",
        tags=[
            "briefcase"
        ]
    )