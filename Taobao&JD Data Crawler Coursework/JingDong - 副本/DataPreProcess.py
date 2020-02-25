import pandas as pd
import numpy as np
import re
def process_brand(x):
    if pd.isnull(x):
        return np.nan
    elif x=='苹果（Apple）':
        return 'Apple'
    elif x=='华为（HUAWEI）':
        return 'HUAWEI'
    elif x=='小米（MI）':
        return 'XIAOMI'
    elif x=='诺基亚（NOKIA）':
        return 'NOKIA'
    elif x=='飞利浦（Philips）':
        return 'Philips'
    elif x=='天语（K-Touch）':
        return 'K-Touch'
    elif x=='魅族（MEIZU）':
        return 'MEIZU'
    elif x=='三星（SAMSUNG）':
        return 'SAMSUNG'
    elif x=='锤子（smartisan）':
        return 'smartisan'
    elif x=='联想（lenovo）':
        return 'lenovo'
    elif x=='美图（Meitu）':
        return 'Meitu'
    elif x=='努比亚（nubia）':
        return 'nubia'
    elif x=='中兴（ZTE）':
        return 'ZTE'
    elif x=='酷派（Coolpad）':
        return 'Coolpad'
    elif x=='其他品牌':
        return np.nan
    elif x=='小辣椒':
        return 'chilli'
    elif x=='黑莓（BlackBerry）':
        return 'BlackBerry'
    else:
        return x

def process_comments(x):
    if pd.isnull(x):
        return np.nan
    else:
        x=x.split('+')[0]
        if '万' in x:
            x=float(x.split('万')[0])
            x=x*10000
        else:
            x=float(x)
        return x
def process_price(x):
    if pd.isnull(x):
        return np.nan
    else:
        x=str(x)
        match=re.search(r'-?\d+\.?\d*e?-?\d*?',x)
        if match:
            x=match.group(0)
            return x
data=pd.read_csv('Explicit_phones_data.csv',encoding='utf-8')
data['brand']=data['brand'].apply(lambda x:process_brand(x))
data['price']=data['price'].apply(lambda  x:process_price(x))
data['comments']=data['comments'].apply(lambda  x:process_comments(x))
data.to_csv("WellProcessed_phones_data.csv")