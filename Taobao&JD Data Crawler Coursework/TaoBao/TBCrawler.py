import os
import re
import json
import time
import random
import requests
import pandas as pd
from retrying import retry
from TBLogger import TaoBaoLogin

requests.packages.urllib3.disable_warnings()
req_session = requests.Session()# 使用同一个Session对象
OUTPUT_FILE = 'Raw_phones_data.xlsx'


class DataSpider:
    def __init__(self, q):
        self.q = q
        # 超时
        self.timeout = 15
        self.goods_list = []
        # 淘宝登录
        tbl = TaoBaoLogin(req_session)
        tbl.login()

    @retry(stop_max_attempt_number=3)
    def spider_goods(self, page):
        s = page * 44
        # 搜索链接，q参数表示搜索关键字，s=page*44 数据开始索引 一页44个数据
        search_url=f'https://s.taobao.com/search?q={self.q}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&s={s}&data-key=s&data-value={s + 44}'
        proxies = {'http': '10.28.234.209:8080',
                   }
        # 请求头
        headers = {
            'referer': 'https://www.taobao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = req_session.get(search_url, headers=headers, proxies=proxies,
                                   verify=False, timeout=self.timeout)
        # print(response.text)
        goods_match = re.search(r'g_page_config = (.*?)}};', response.text)
        # 没有匹配到数据
        if not goods_match:
            print('提取页面中的数据失败！')
            print(response.text)
            raise RuntimeError
        goods_str = goods_match.group(1) + '}}'
        goods_list = self._get_goods_info(goods_str)
        self._save_excel(goods_list)
        # print(goods_str)

    def _get_goods_info(self, goods_str):
        """
        解析json数据，并提取标题、价格、商家地址、销量、评价地址
        """
        goods_json = json.loads(goods_str)
        goods_items = goods_json['mods']['itemlist']['data']['auctions']
        goods_list = []
        for goods_item in goods_items:
            goods = {'title': goods_item['raw_title'],
                     'price': goods_item['view_price'],
                     'location': goods_item['item_loc'],
                     'sales': goods_item['view_sales'],
                     'comment_url': goods_item['comment_url']}
            goods_list.append(goods)
            print(goods)
        return goods_list

    def _save_excel(self, goods_list):
        """
        将json数据生成excel文件
        :param goods_list: 商品数据
        :param startrow: 数据写入开始行
        :return:
        """
        # pandas没有对excel没有追加模式，只能先读后写
        if os.path.exists(OUTPUT_FILE):
            df = pd.read_excel(OUTPUT_FILE)
            df = df.append(goods_list)
        else:
            df = pd.DataFrame(goods_list)

        writer = pd.ExcelWriter(OUTPUT_FILE)
        # columns参数用于指定生成的excel中列的顺序
        df.to_excel(excel_writer=writer, columns=['title', 'price', 'location', 'sales', 'comment_url'], index=False,
                    encoding='utf-8', sheet_name='Sheet')
        writer.save()
        writer.close()

    def patch_spider_goods(self):
        # 写入数据前先清空之前的数据
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
        for i in range(0, 30):
            print('第%d页' % (i + 1))
            self.spider_goods(i)
            # 设置一个时间间隔
            time.sleep(random.randint(25, 30))


if __name__ == '__main__':
    Crawler = DataSpider('手机')
    Crawler.patch_spider_goods()
