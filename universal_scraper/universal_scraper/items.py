import scrapy


class BookItem(scrapy.Item):

    title = scrapy.Field()

    price = scrapy.Field()

    stock = scrapy.Field()