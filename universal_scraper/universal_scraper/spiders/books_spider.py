import scrapy

from universal_scraper.items import BookItem


class BooksSpider(scrapy.Spider):

    name = "books"

    allowed_domains = [
        "books.toscrape.com"
    ]

    start_urls = [
        "https://books.toscrape.com"
    ]

    def parse(self, response):

        books = response.css(
            "article.product_pod"
        )

        for book in books:

            item = BookItem()

            item["title"] = book.css(
                "h3 a::attr(title)"
            ).get()

            item["price"] = book.css(
                ".price_color::text"
            ).get()

            item["stock"] = "".join(
                book.css(
                    ".instock.availability ::text"
                ).getall()
            ).strip()

            yield item

        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:

            yield response.follow(
                next_page,
                callback=self.parse
            )