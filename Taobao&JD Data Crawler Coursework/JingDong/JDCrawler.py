import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from lxml import html
import pandas as pd
import time
import numpy as np

browser = webdriver.Chrome()
phone_list=[]
pageCounter=0
dic={}

for i in range(22):
    #   JD按照评论数排序
    browser.get("https://list.jd.com/list.html?cat=9987,653,655&page={}&sort=sort_commentcount_desc".format(i+1))
    wait = WebDriverWait(browser, 10)
    page=html.fromstring(browser.page_source)
    print("Start visiting No.{} external pages,progress:".format(i))
    count=0
    print("[[",end='')
    for each in page.xpath("//div[@class='gl-i-wrap j-sku-item']"):
        count+=1
        if count%6==0:
            print('===',end='')
        phone_id=each.xpath("./@data-sku")[-1]
        price=each.xpath(".//div[@class='p-price']/strong[1]/i/text()")[:]
        comments=each.xpath(".//a[@class='comment']/text()")[-1]
        phone_list.append(list((phone_id,price,comments)))
    print("]]",end='')
    print("\nNo.{} external pages have been visited.".format(i))
browser.close()
to_save=pd.DataFrame(phone_list)
middle="phone_id,price,comments"
print("***********************************{}have been written into Raw_phones_data.csv **"
      "*********************************".format(middle))
to_save.to_csv('Raw_phones_data.csv')



df=pd.read_csv('Raw_phones_data.csv')
phone_list=[]
df=df.set_index(['PhoneID'])
for i in range(df.shape[0]):
    phone_list.append(df.iloc[i,:].values)

for each in phone_list:
    url='https://item.jd.com/{}.html'.format(each[0])
    r=requests.get(url)
    if r.ok==False:
        print('不允许访问,出错!')
        break
    page=html.fromstring(r.text)
    dic_temp={}
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='电池容量（mAh）']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['battery']=list_temp[-1]
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='上市年份']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['year']=list_temp[-1]
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='上市月份']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['month']=list_temp[-1]
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='品牌']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['brand']=list_temp[-1]
    # //*[@id="detail"]/div[2]/div[2]/div[1]/div[1]/dl/dl[3]/dd
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='产品名称']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['model']=list_temp[-1]
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='机身重量（g）']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['weight']=list_temp[-1]
    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU型号']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['CPU model']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU频率']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['CPU freq']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='CPU核数']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['CPU cores']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='最大支持SIM卡数量']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['SIM cards']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='ROM']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['ROM']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='RAM']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['RAM']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='主屏幕尺寸（英寸）']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['screen size']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='分辨率']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['resolution']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='屏幕材质类型']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['screen material']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='前置摄像头']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['front camera']=list_temp[-1]

    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='摄像头数量']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['rear camera']=list_temp[-1]


    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='后置摄像头']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['rear camera specs']=list_temp[-1]


    list_temp=page.xpath("//dl[@class='clearfix'][./dt[text()='充电接口类型']]/dd/text()")
    list_temp.insert(0,np.nan)
    dic_temp['charging port']=list_temp[-1]

    dic_temp['price']=each[1]
    dic_temp['comments']=each[2]

    dic[each[0]]=dic_temp

    pageCounter+=1
    if pageCounter%60==0:
        print(pageCounter,' inner pages have been written.Stop for a while')
        time.sleep(12)
    time.sleep(0.5)

finaldf=pd.DataFrame(dic).T
finaldf.to_csv('Explicit_phones_data.csv')
