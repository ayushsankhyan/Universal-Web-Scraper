class UniversalScraperPipeline:

    def process_item(
        self,
        item,
        spider
    ):

        item["title"] = (
            item["title"]
            .strip()
        )

        item["price"] = (
            item["price"]
            .replace("£", "")
            .strip()
        )

        item["stock"] = (
            item["stock"]
            .strip()
        )

        return item