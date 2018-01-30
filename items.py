# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CordisnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Cordis news
    Title = Field()
    Teaser = Field()
    Article = Field()
    Subject = Field()
    Countries = Field()

    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
