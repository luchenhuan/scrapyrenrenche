# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class renrencheItem(Item):

    title = Field()
    price = Field()
    new_car_price = Field()
    deposit = Field()
    payment = Field()
    service_pay = Field()
    city = Field()
    car_summary = Field()
    gearbox = Field()
    transfer_record = Field()
    url = Field()


