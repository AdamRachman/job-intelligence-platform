import re


# ==========================================================
# Clean Text
# ==========================================================

def clean_text(text):

    if text is None:
        return None

    text = str(text)

    text = text.replace("\xa0", " ")

    text = text.replace("\r", " ")

    text = text.replace("\t", " ")

    text = text.replace("\n", " ")

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()

# ==========================================================
# Remove Surrounding Parentheses
# ==========================================================

def clean_parentheses(text):

    if text is None:
        return None

    text = str(text).strip()

    if (
        text.startswith("(")
        and
        text.endswith(")")
    ):
        text = text[1:-1]

    return text.strip()