from src.transform.cleaners import (
    clean_text,
    clean_parentheses
)


def main():

    print("=" * 60)
    print("CLEANERS TEST")
    print("=" * 60)

    text = "  Hello\xa0\n\tWorld   "

    result = clean_text(text)

    print(result)

    assert result == "Hello World"

    print("[PASS] clean_text")

    text = "(Teknologi Informasi & Komunikasi)"

    result = clean_parentheses(text)

    print(result)

    assert result == "Teknologi Informasi & Komunikasi"

    print("[PASS] clean_parentheses")


if __name__ == "__main__":

    main()