from bs4 import BeautifulSoup
from collections import Counter


def extract_text(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    class_counter = Counter()

    for tag in soup.find_all():

        classes = tag.get("class")

        if classes:

            class_name = " ".join(classes)

            class_counter[class_name] += 1

    best_class = None
    best_score = 0

    for class_name, count in class_counter.items():

        if count < 3:
            continue

        elements = soup.find_all(
            class_=class_name.split()
        )

        text_lengths = []

        for element in elements:

            text = element.get_text(
                " ",
                strip=True
            )

            if len(text) > 20:

                text_lengths.append(
                    len(text)
                )

        if not text_lengths:
            continue

        avg_length = (
            sum(text_lengths)
            / len(text_lengths)
        )

        score = (
            count * avg_length
        )

        layout_words = [
            "row",
            "container",
            "wrapper",
            "grid",
            "col-"
        ]

        if any(
            word in class_name.lower()
            for word in layout_words
        ):
            score *= 0.3

        if score > best_score:

            best_score = score
            best_class = class_name

    print(
        "\nSELECTED:",
        best_class
    )

    if not best_class:
        return []

    records = []

    elements = soup.find_all(
        class_=best_class.split()
    )

    for element in elements:

        text = element.get_text(
            " ",
            strip=True
        )

        if len(text) < 20:
            continue

        records.append(
            text
        )

    records = list(
        dict.fromkeys(records)
    )

    return records