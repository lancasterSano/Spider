import scrapy


class DmozItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass

    def square(self, x):
        x_square = x * x
        return x_square

