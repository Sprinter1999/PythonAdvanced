# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyPipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open("MyData.json", "w", encoding="utf-8")
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) #生成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + "\n" #生成json串
        self.file.write(json_str) #将json串写入到文件中
        return item
    
    def close_spider(self, spider):
        self.file.close()
