# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field();
    location1=scrapy.Field();
    location2 = scrapy.Field();
    location3 = scrapy.Field();
    huxing=scrapy.Field();
    area=scrapy.Field();
    totality=scrapy.Field();
    meanPrice=scrapy.Field();
