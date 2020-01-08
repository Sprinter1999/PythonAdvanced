import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#打开csv文件
fileNameStr = 'dealsecondhand.csv'
orig_df = pd.read_csv(fileNameStr,encoding='utf-8',dtype=str)

#1.将name,information,totalprice,unitprice列去掉空格
orig_df['name'] = orig_df['name'].str.strip()
orig_df['information'] = orig_df['information'].str.strip()
orig_df['totalprice'] = orig_df['totalprice'].str.strip()
orig_df['unitprice'] = orig_df['unitprice'].str.strip()

#2.处理unitprice中的字
orig_df['unitprice'] = orig_df['unitprice'].str.replace("单价","")
orig_df['unitprice'] = orig_df['unitprice'].str.replace("元/平米","")

#3.将后两列转为整数，总价乘10000
orig_df['unitprice'] = orig_df['unitprice'].astype(np.int)
orig_df['totalprice'] = orig_df['totalprice'].astype(np.float)
orig_df['totalprice'] = orig_df['totalprice'].astype(np.int)
orig_df['totalprice'] = orig_df['totalprice'] * 10000

#4.输出到文件
orig_df.to_csv("dealsecondhand.csv",encoding = 'gbk')
