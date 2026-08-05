# ==========================
# Notification Parameters
# ==========================

# UBAH PARAMETER NOTIFIKASI

TARGET_ROLES = [
    "data engineer",
]


TARGET_SENIORITY = [
    "associate",
    "entry level",
]


# ==========================
# Notification Rules
# ==========================

def should_notify(job):

    title = str(
        job.get("title", "")
    ).lower()


    seniority = str(
        job.get("seniority_level", "")
    ).lower()


    role_match = any(
        role in title
        for role in TARGET_ROLES
    )


    seniority_match = any(
        level in seniority
        for level in TARGET_SENIORITY
    )


    return (
        role_match
        and
        seniority_match
    )