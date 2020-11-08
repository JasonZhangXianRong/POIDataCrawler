# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PoidatacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    address = scrapy.Field()
    class1 = scrapy.Field()
    class2 = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
