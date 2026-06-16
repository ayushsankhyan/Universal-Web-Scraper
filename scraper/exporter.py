import csv
import os


def save_csv(records):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        "data/results.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Record"]
        )

        for record in records:

            writer.writerow(
                [record]
            )

    print(
        f"Saved {len(records)} records to data/results.csv"
    )