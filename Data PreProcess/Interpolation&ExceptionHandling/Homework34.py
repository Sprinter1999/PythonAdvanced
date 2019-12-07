#!/usr/bin/env python
# coding: utf-8

# # 数据预处理-2
# 
# - 班级:2017211314
# - 学号:2017213508
# - 学生:蒋雪枫
# 
# ## 作业3

# **一些额外的Trick:**
# #比如想要产生新的一列来统计同一时间内所有地方的PM指数和
# df['sumOfPM']=df['PM_US_POST']+df['PM_Nongzhanguan']+df['PM_Dongsi']+df['PM_Dongsihuan']
# #比如想要按照某一列排序,升序
# def top(df,n=5,colunm='PRES'):
#     return df.sort_values(by=column)[-n:]
# #apply函数是`pandas`里面所有函数中自由度最高的函数。该函数如下：
# DataFrame.apply(func, axis=0, broadcast=False, raw=False...)
# 该函数最有用的是第一个参数，这个参数是函数，相当于C/C++的函数指针。
# 
# #这次预处理实验和上次预处理实验后,我明显感受到直接按列操作比遍历每一个csv中的cell效率高得多,减小了IO时间

# In[1]:


import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

df = pd.read_csv("BeijingPM20100101_20151231.csv",encoding='utf-8')
df.describe()


# In[2]:


todo = ['HUMI', 'PRES', 'TEMP']
#进行线性插值
for each in todo:
    df[each]=df[each].interpolate(method="linear")
print("将dataframe其中一列抽出来是什么类型?{}".format(type(df['HUMI'])))
for each in todo:
    mean = df[each].mean()
    stdDoub = df[each].std()
    df[each]= df[each].apply(lambda x : mean + stdDoub*2 if x>mean + stdDoub * 2 
                                  else ( mean-2 * stdDoub if x < mean -  2 * stdDoub else x))


# In[3]:


todo = ['PM_Dongsi','PM_Dongsihuan','PM_Nongzhanguan']
print("处理前")
#   PM:6,7,8,9 || HUMI PRES TEMP:11,12,13 || cbwd:14
print(df.iloc[30590:30600,6:9])
for each in todo:
    df[each] = df[each].apply(lambda x: 500 if x > 500 else x)
print("处理后")
print(df.iloc[30590:30600,6:9])


# In[4]:


#下面第一种方式比较直观,但如果出现两个连续的cv,怎么处理?  
# Excel里面也告诉我们的确出现了
# for i in range(len(df['cbwd'])):
#     if df['cbwd'][i] == 'cv':
#         df.at[i:i,'cbwd'] =  df['cbwd'][i+1]
print("对CV处理前")
print(df.iloc[20:25,8:15])
print("对CV处理后")
#TODO:采用bfill替换方式
df['cbwd']=df['cbwd'].replace('cv',method='bfill')
print(df.iloc[20:25,8:15])


# In[5]:


df.describe() 


# In[6]:


df.to_csv("result.csv")


# ####  比较前后的描述信息,可以较为明显地看出有关标准差采取的措施带来的改变

# ## 作业4

# In[7]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
features = ['DEWP', 'TEMP']
df[features] = scaler.fit_transform(df[features])
df.head()
df.plot.scatter(x=['DEWP'],y=['TEMP'],s=10,figsize = (20,20))


# In[8]:


from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
features = ['DEWP', 'TEMP']
df[features] = ss.fit_transform(df[features])
df.head()
df.plot.scatter(x=['DEWP'],y=['TEMP'],s=10,figsize = (20,20))


# In[9]:


sections = [0,50,100,150,200,300,1200] #划分为不同长度 的区间 
section_names=["green","yellow","orange","red","purple", "Brownish red"] #设置每个区间的标签
# df = df.fillna(df.mean())
result = pd.cut(df.PM_Dongsi,sections,labels=section_names) 
print(pd.value_counts(result))

