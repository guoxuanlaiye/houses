# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    houses_name = scrapy.Field()
    houses_adress = scrapy.Field()
    average_price = scrapy.Field()
    around_ava_price = scrapy.Field()
    price_status = scrapy.Field()
    tags = scrapy.Field()
    houses_type = scrapy.Field()
    houses_area = scrapy.Field()


