import numpy as np
import pandas as pd
import time

#1.打开CSV文件
fileNameStr = 'ShenyangPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[0,1,2,3,4,5,6,7,8])

print(df.head())
print(df.describe())
print(df.info())
print("================================")
#2.查看是否有缺失值
print(df.isnull().sum().sort_values(ascending=False))
print("================================")

#方案二，直接使用dataframe的方法
#3.去掉三列PM数据全部为空的行
print(df.info())
df.dropna(axis='index', how='all', subset=['PM_Taiyuanjie','PM_US Post','PM_Xiaoheyan'], inplace=True)

print("**************************")
print(df.info())
#df.to_csv("sy.csv")

#4.计算平均值
start = time.time()
df['sum'] = df[['PM_Taiyuanjie','PM_Xiaoheyan','PM_US Post']].sum(axis=1)
df['count'] = df[['PM_Taiyuanjie','PM_Xiaoheyan','PM_US Post']].count(axis=1)
df['ave']=round(df['sum']/df['count'],2)
end = time.time()
print("---------------duration:",end-start)

#5.输出到文件
df.to_csv("shenyang_ave.csv")
print("****** done ******")

#6.按照年做汇总，查看年的平均值
print(df.groupby("year").mean())


