# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppstoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    app_id = scrapy.Field()
    intro = scrapy.Field()
    recommended = scrapy.Field()
    developer = scrapy.Field()
    thumbnail_url = scrapy.Field()
    score = scrapy.Field()
