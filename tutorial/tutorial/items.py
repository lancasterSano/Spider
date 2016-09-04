import scrapy


class DmozItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass
