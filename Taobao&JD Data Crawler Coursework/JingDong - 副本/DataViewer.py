import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Rank_phones.csv",encoding='gbk')
df.dropna(axis=0, how='any', inplace=True)
df.to_csv("DropNull_Rank_phones.csv")


plt.rcParams['font.sans-serif'] = ['SimHei']
filenamestr = 'DropNull_Rank_phones.csv'
df = pd.read_csv(filenamestr,encoding='utf-8')

# 2.统计型号对应的销量、价格对应的商家数
count_sale = {}
count_price = {}
for i in range(0, len(df['title'])):
    if count_sale.get(str(df['title'].values[i])) is None:
        count_sale[str(df['title'].values[i])] = 0
    if count_price.get(int(df['price'].values[i])) is None:
        count_price[int(df['price'].values[i])] = 0

    count_sale[str(df['title'].values[i])] += int(df['comments'].values[i])
    count_price[int(df['price'].values[i])] += 1

# 3.筛选销量前20的手机型号，并作图
count_sale2 = sorted(count_sale.items(), key=lambda x: x[1], reverse=True)
print(count_sale2)
x = []
y = []
plt.xlabel("型号",fontsize=4)
plt.ylabel("评论数",fontsize=4)
plt.tick_params(labelsize=5)
for i in range(0,20):
    print("第",i+1,"名:",count_sale2[i][0],",评论数:",count_sale2[i][1])
    x.append(count_sale2[i][0])
    y.append(count_sale2[i][1])
plt.bar(x, y,color='g')
plt.show()

# 4.画价格对应的散点图
plt.xlabel("评论数",fontsize=10,fontweight='bold')
plt.ylabel("商家",fontsize=10,fontweight='bold')
price = count_price.keys()
values = count_price.values()
plt.scatter(price,values,color='g')
plt.show()

# 5.画箱型图
phone1 = []
phone2 = []
phone3 = []
phone4 = []
phone5 = []
# Honor 20
for i in range(0, len(df['title'])):
    if df['title'].values[i] == 'Honor 8X':
        phone1.append(df['price'].values[i])
    if df['title'].values[i] == 'iPhone XR':
        phone2.append(df['price'].values[i])
    if df['title'].values[i] == 'iPhone 8 Plus':
        phone3.append(df['price'].values[i])
    if df['title'].values[i] == 'iPhone 8':
        phone4.append(df['price'].values[i])
    if df['title'].values[i] == 'Honor 10':
        phone5.append(df['price'].values[i])


print(phone1, phone5)
data = pd.DataFrame({
    'Honor 8X':phone1,
})
data2 = pd.DataFrame({
    'iPhone XR':phone2,
})
data3 = pd.DataFrame({
    'iPhone 8 Plus':phone3,
})
data4 = pd.DataFrame({
    'iPhone 8':phone4,
})
data5 = pd.DataFrame({
    'Honor 10':phone5,
})

# 五个子图
plt.subplot(1,5,1)
data.boxplot()
plt.subplot(1,5,2)
data2.boxplot()
plt.subplot(1,5,3)
data3.boxplot()
plt.subplot(1,5,4)
data4.boxplot()
plt.subplot(1,5,5)
data5.boxplot()
plt.show()
