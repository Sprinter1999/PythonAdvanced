import scrapy
from Xuetang.items import MyItem #从items.py中引入MyItem对象
class mySpider(scrapy.spiders.Spider):
    name = "Xuetang" #爬虫的名字是bupt
    allowed_domains = ["http://www.xuetangx.com/"] #允许爬取的网站域名
    start_urls = ["http://www.xuetangx.com/partners"]
    #初始URL，即爬虫爬取的第一个URL
    # /html/body/article[1]/section/ul
    def parse(self,response):
        item=MyItem()
        for each in response.xpath("/html/body/article[1]/section/ul/li/a/div[2]"):
            # /html/body/article[1]/section/ul/li[1]/a/div[1]/span/img
            # /html/body/article[1]/section/ul
            item['name']=each.xpath("h3/text()").extract()
            item['number']=each.xpath("p[1]/text()").extract()
            if(item['name'] and item['number']):  # 去掉值为空的数据
                yield(item)