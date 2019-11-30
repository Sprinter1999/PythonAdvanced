import scrapy
import re
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

            item['name']=each.xpath("a/@title").extract()#/html/body/div[4]/ul[2]/li[1]/a
            item['location1']=each.xpath("div/div[2]/span[1]/text()").extract()#/html/body/div[4]/ul[2]/li[1]/div/div[2]/span[1]
            item['location2'] = each.xpath("div/div[2]/span[2]/text()").extract()#/html/body/div[4]/ul[2]/li[1]/div/div[2]/span[2]
            item['location3'] = each.xpath("div/div[2]/a/text()").extract()#/html/body/div[4]/ul[2]/li[1]/div/div[2]/a
            item['huxing']=each.xpath("div/a/span[1]/text()").extract()#/html/body/div[4]/ul[2]/li[1]/div/a/span[1]
            item['area']=each.xpath("div/div[3]/span/text()").extract()#/html/body/div[4]/ul[2]/li[1]/div/div[6]/div[2]
            item['totality']=each.xpath("div/div[6]/div[2]/text()").extract();
            item['meanPrice']=each.xpath("div/div[6]/div[1]/span[1]/text()").extract()
            if(item['area']):
                match1=re.search(r'[0-9]+',item['area'][0])
                if match1:
                    item['area'][0]=eval(match1.group(0))
            if(item['totality']):
                match1=re.search(r'[0-9]+',item['totality'][0])
                if match1:
                    item['totality'][0]=eval(match1.group(0))
            if(item['meanPrice']):
                match1=re.search(r'[0-9]+',item['meanPrice'][0])
                if match1:
                    item['meanPrice'][0]=eval(match1.group(0))
                if(item['meanPrice'][0]<10000):
                    item['meanPrice'][0]=round(item['totality'][0]*10000/item['area'][0],4)
            yield(item)