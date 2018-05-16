# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .sql import sql
from .sql.sql import Houses

'''
houses_name
houses_adress
average_price
around_ava_price
price_status
tags
houses_type
houses_area
'''
class AnjukePipeline(object):
    def process_item(self, item, spider):

        session = sql.DBSession()
        house = Houses(houses_name=item["houses_name"], houses_adress=item["houses_adress"], average_price=item["average_price"], around_ava_price=item["around_ava_price"], price_status=item["price_status"], tags=item["tags"], houses_type=item["houses_type"], houses_area=item["houses_area"])
        session.add(house)
        session.commit()
        session.close()

        return item
