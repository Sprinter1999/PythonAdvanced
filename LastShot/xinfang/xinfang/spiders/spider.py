import scrapy
from xinfang.items import XinfangItem

class xinfangSpider(scrapy.spiders.Spider):
    name = "fuck"
    allowed_domains = ["sz.lianjia.com/"]

    start_urls = []
    for page in range(1,100):
        url = "https://sz.lianjia.com/ershoufang/pg{}/".format(page)

        start_urls.append(url)

    def parse(self,response):
        item = XinfangItem()
        for i in range(1,30):
            item['name'] = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[1]/a/text()'.format(i)).extract()
            item['information'] = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[3]/div/text()'.format(i)).extract()
            item['totalprice'] = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[6]/div[1]/span/text()'.format(i)).extract()
            item['unitprice'] = response.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]/div[6]/div[2]/span/text()'.format(i)).extract()

            if(item['name'] and item['information'] and item['totalprice'] and item['unitprice']):
                yield (item)

