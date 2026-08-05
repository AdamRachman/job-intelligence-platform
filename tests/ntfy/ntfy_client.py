from src.notification.ntfy_client import (
    send_notification,
)


def main():

    send_notification(

        title=(
            "Job Intelligence Test"
        ),

        message=(
            "ntfy integration from "
            "VS Code is working."
        ),

        priority="high",

        tags=[
            "briefcase",
        ],

    )


if __name__ == "__main__":

    main()