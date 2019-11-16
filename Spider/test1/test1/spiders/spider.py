import scrapy
from test1.items import MyItem
class mySpider(scrapy.spiders.Spider):
    name = "bupt" #爬虫名字
    allowed_domains = ["bupt.edu.cn/"] #允许爬取的网站域名
    start_urls = ["https://www.bupt.edu.cn/yxjg1.htm"]
    #初始url，即爬虫爬取的第一个url
    def parse(self, response): #解析爬取的内容
        item = MyItem() #生成一个在items.py中定义好的myitem对象，用于接收爬虫数据
        # / html / body / div / div[2] / div[2] / div / ul / li[4] / div / *
        for each in response.xpath("/html/body/div/div[2]/div[2]/div/ul/li[4]"):
            #用xpath解析html，div标签中的数据，即我们需要的数据
            item['school'] = each.xpath("text()").extract() #学院名称在text中
            item['link'] = each.xpath("@href").extract() #学院链接在href中
            if(item['school'] and item['link']): #去掉值为空的数据
                yield(item) #返回item数据给到pipelines模块