import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

#1.打开CSV文件
fileNameStr = 'dealsecondhand.csv'
df = pd.read_csv(fileNameStr,encoding='gbk')

#2.查看总价和均价的统计量分析
print(df.describe())
#生成箱型图
df.boxplot(column='unitprice')
plt.show()
f = df.boxplot(column='totalprice',meanline=True,showmeans=True,return_type='dict')
#画出均值线
for mean in f['means']:
    mean.set(color='r', linewidth=3)
plt.show()

