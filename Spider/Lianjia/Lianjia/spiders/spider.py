import scrapy
from Lianjia.items import MyItem #从items.py中引入MyItem对象
class mySpider(scrapy.spiders.Spider):
    name = "Lianjia" #爬虫的名字是bupt
    allowed_domains = ["https://bj.fang.lianjia.com/loupan/"] #允许爬取的网站域名
    start_urls = ["https://bj.fang.lianjia.com/loupan/nhs1pg1/","https://bj.fang.lianjia.com/loupan/nhs1pg2/",
                  "https://bj.fang.lianjia.com/loupan/nhs1pg3/","https://bj.fang.lianjia.com/loupan/nhs1pg4/",
                  "https://bj.fang.lianjia.com/loupan/nhs1pg5/"]
    #初始URL，即爬虫爬取的第一个URL
    # /html/body/article[1]/section/ul
    def parse(self,response):
        item=MyItem()
        for each in response.xpath("/html/body/div[4]/ul[2]/*"):
            # /html/body/div[4]/ul[2]/li[1]/div
            # /html/body/div[4]/ul[2]/li[1]
            # /html/body/div[4]/ul[2]/li[1]/div
            # /html/body/div[4]/ul[2]/li[1]/div/div[1]/a

            # /html/body/div[4]/ul[2]/li[1]/
            # /html/body/div[4]/ul[2]/li[1]/a
            # /html/body/div[4]/ul[2]/li[1]/div/div[6]/div[1]/span[1]
            item['name']=each.xpath("a/@title").extract()
            item['square']=each.xpath("div/div[3]/span/text()").extract()
            item['price']=each.xpath("div/div[6]/div[1]/span[1]/text()").extract()
            # if(item['name'] and item['square'] and item['price']):  # 去掉值为空的数据
            yield(item)