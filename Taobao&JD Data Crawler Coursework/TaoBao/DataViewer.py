import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
filenamestr = 'Rank_phones.csv'
df = pd.read_csv(filenamestr, encoding='gbk')
count_sale = {}
count_price = {}

def DataViewer():
    # 2.统计型号对应的销量、价格对应的商家数
    for i in range(0, len(df['title'])):
        if not(count_sale.get(str(df['title'].values[i]))):
            count_sale[str(df['title'].values[i])] = 0
        if not(count_price.get(int(df['price'].values[i]))):
            count_price[int(df['price'].values[i])] = 0

        count_sale[str(df['title'].values[i])] += int(df['sales'].values[i])
        count_price[int(df['price'].values[i])] += 1

    # 3.筛选销量前20的手机型号，并作图
    Top20 = sorted(count_sale.items(), key=lambda x: x[1], reverse=True)
    print(Top20)
    x,y= [],[]
    plt.xlabel("款式",fontsize=5)
    plt.ylabel("销量",fontsize=5)
    plt.tick_params(labelsize=6)
    for i in range(0,20):
        print("第", i + 1, "名:", Top20[i][0], ",评论数:", Top20[i][1])
        x.append(Top20[i][0])
        y.append(Top20[i][1])
    plt.bar(x, y,color='g',width=0.5,align='edge')
    plt.show()

    # 4.画价格对应的散点图
    plt.xlabel("MinPrice",fontsize=8)
    plt.ylabel("ShopNum",fontsize=8)
    price = count_price.keys()
    values = count_price.values()
    plt.scatter(price,values,color='g',edgecolors='b')
    plt.show()

    # 5.画箱型图
    phone1,phone2,phone3,phone4,phone5 = [],[],[],[],[]
    # Honor 20
    for i in range(0, len(df['title'])):
        if df['title'].values[i] == 'Huawei Honor 20':
            phone1.append(df['price'].values[i])
        if df['title'].values[i] == 'Huawei Nova 5':
            phone2.append(df['price'].values[i])
        if df['title'].values[i] == 'Huawei Mate 30':
            phone3.append(df['price'].values[i])
        if df['title'].values[i] == 'iPhone 8':
            phone4.append(df['price'].values[i])
        if df['title'].values[i] == 'Vivo Z5':
            phone5.append(df['price'].values[i])


    data = pd.DataFrame({
        'Huawei Honor 20':phone1,
    })
    data2 = pd.DataFrame({
        'Huawei Nova 5':phone2,
    })
    data3 = pd.DataFrame({
        'Huawei Mate 30':phone3,
    })
    data4 = pd.DataFrame({
        'iPhone 8':phone4,
    })
    data5 = pd.DataFrame({
        'Vivo Z5':phone5,
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

if __name__=="__main__":
    DataViewer()
