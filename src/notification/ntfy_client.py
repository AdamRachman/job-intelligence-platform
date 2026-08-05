import requests

from src.config.settings import (
    NTFY_BASE_URL,
    NTFY_TOPIC,
    NTFY_TIMEOUT,
)


def send_notification(
    title,
    message,
    priority="default",
    tags=None,
):

    url = (
        f"{NTFY_BASE_URL}/{NTFY_TOPIC}"
    )

    headers = {
        "Title": title,
        "Priority": priority,
    }

    if tags:

        headers["Tags"] = ",".join(
            tags
        )

    response = requests.post(
        url,
        data=message.encode("utf-8"),
        headers=headers,
        timeout=NTFY_TIMEOUT,
    )

    response.raise_for_status()

    print(
        "[PASS] ntfy notification sent"
    )