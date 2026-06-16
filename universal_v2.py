from scraper.fetcher import fetch_page
from scraper.parser import extract_text

from scraper.db import (
    create_table,
    save_product
)

from scraper.product_parser import (
    extract_product_fields
)

from scraper.exporter import save_csv


def main():

    create_table()

    url = input(
        "Enter URL: "
    )

    print(
        "\nFetching page..."
    )

    html = fetch_page(
        url
    )

    print(
        "Extracting records..."
    )

    records = extract_text(
        html
    )

    print(
        f"\nFound {len(records)} records\n"
    )

    if not records:

        print(
            "No records found."
        )

        return

    save_csv(
        records
    )

    saved = 0

    for record in records:

        fields = extract_product_fields(
            record
        )

        save_product(
            url=url,
            title=fields["title"],
            price=fields["price"],
            stock=fields["stock"],
            raw_record=record
        )

        saved += 1

    print(
        f"Saved {saved} records to PostgreSQL."
    )


if __name__ == "__main__":
    main()