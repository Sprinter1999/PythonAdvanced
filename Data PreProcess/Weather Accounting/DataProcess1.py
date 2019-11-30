import numpy as np
import pandas as pd

#打开CSV文件
fileNameStr = 'mydata-hd.csv'
orig_df = pd.read_csv(fileNameStr,encoding='utf-8',dtype=str)

print(orig_df.describe())
print(orig_df.info())
print("================================")
#查看是否有缺失值
print(orig_df.isnull().sum().sort_values(ascending=False))
#按照价格倒排序
print(orig_df.sort_values(by='price',ascending=False))
print("================================")

#1.将name列去掉空格
orig_df['name']=orig_df['name'].str.strip()
orig_df['name.1']=orig_df['name.1'].str.strip()
'''
df1 = orig_df['name'].str.split('|',expand=True)
print(df1)
df1[0]=df1[0].str.strip()
df1[1]=df1[1].str.strip()
'''
#2.将price变为整型
print(orig_df['price'])
orig_df['price'] = orig_df['price'].astype(np.float)

#3.将desp列分列，分列符号为'|'
df = orig_df['desp'].str.split('|',expand=True)
print(df)
#将每一列分别去掉空格
df[0]=df[0].str.strip()
df[1]=df[1].str.strip()
df[2]=df[2].str.strip()
df[3]=df[3].str.strip()
df[4]=df[4].str.strip()
df[5]=df[5].str.strip()
df[6]=df[6].str.strip()
#df.dropna(axis=0, how='any', inplace=True)
#将面积列中的平米去掉
df[1]=df[1].str.replace("平米","")
#将面积列字符串改为数字
df[1] = df[1].astype(np.float)
#将朝向列内容中，中间的空格去掉
df[2]=df[2].str.replace(" ","")
df[5]=df[5].str.replace("年建","")
#if( df[pd.isnull(df[5])].bool == False):
#    df[5]=df[5].astype(np.int)
#print(df)
#去掉无用的第0列
print('----------------------------------------------')
df.drop([7],axis=1,inplace=True)
print(df)
print('----------------------------------------------')
#unitprice=(df.price.astype(np.float))
#计算单价
unitprice=round(orig_df['price']/df[1],4)
#print(unitprice)
df["district"]="海淀"
#合并原始数据的某些列，与分拆后的新列，以及计算出来的新列
result = pd.concat([orig_df['name'],orig_df['name.1'],df,orig_df.price,unitprice],axis=1,ignore_index=True)
result.columns = ['name','loc','type','area','direction','decoration','level','year','building_type','district','totalprice','unitprice']
result.sort_values(by='unitprice',ascending=False,inplace=True)
#df.to_csv("lj2.csv",encoding="gbk")
result.to_csv("result-hd.csv",encoding="utf-8")

print(result.describe())

