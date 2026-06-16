import re


def extract_product_fields(record):

    title = record
    price = ""
    stock = ""

    price_match = re.search(
        r"£\d+\.\d+",
        record
    )

    if price_match:

        price = price_match.group()

        title = record.split(
            price
        )[0].strip()

    if "In stock" in record:

        stock = "In stock"

    return {
        "title": title,
        "price": price,
        "stock": stock
    }