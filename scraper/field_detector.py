import re


def detect_fields(text):

    fields = {}

    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email_match:

        fields["email"] = (
            email_match.group()
        )

    phone_match = re.search(
        r"\+?\d[\d\s\-()]{7,}",
        text
    )

    if phone_match:

        fields["phone"] = (
            phone_match.group()
        )

    url_match = re.search(
        r"https?://[^\s]+",
        text
    )

    if url_match:

        fields["url"] = (
            url_match.group()
        )

    price_match = re.search(
        r"[£$€₹]\s?\d+(?:\.\d+)?",
        text
    )

    if price_match:

        fields["price"] = (
            price_match.group()
        )

    return fields