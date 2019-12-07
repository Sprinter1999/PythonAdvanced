import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
#1.打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',dtype=str)
#2010 0101 - 2015 1231
#6年 12个月
print("info============================================================================")
print(df.info())
print("=======================================")
start = time.time()
account=[[0 for i in range(13)] for j in range(6)]
counters=[[0 for i in range(13)] for j in range(6)]
for i in range(52584):
    if(eval(df['year'][i])==2010):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[0][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[0][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[0][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[0][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[0][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[0][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[0][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[0][eval(df['month'][i])]+=1
    elif(eval(df['year'][i])==2011):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[1][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[1][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[1][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[1][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[1][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[1][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[1][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[1][eval(df['month'][i])]+=1
    elif(eval(df['year'][i])==2012):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[2][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[2][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[2][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[2][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[2][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[2][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[2][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[2][eval(df['month'][i])]+=1
    elif(eval(df['year'][i])==2013):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[3][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[3][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[3][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[3][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[3][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[3][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[3][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[3][eval(df['month'][i])]+=1
    elif(eval(df['year'][i])==2014):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[4][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[4][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[4][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[4][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[4][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[4][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[4][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[4][eval(df['month'][i])]+=1
    elif(eval(df['year'][i])==2015):
        if not(df['PM_Dongsi'][i] is np.nan):
            account[5][eval(df['month'][i])]+=int(df['PM_Dongsi'][i])
            counters[5][eval(df['month'][i])]+=1
        if not (df['PM_Dongsihuan'][i] is np.nan):
            account[5][eval(df['month'][i])]+=int(df['PM_Dongsihuan'][i])
            counters[5][eval(df['month'][i])]+=1
        if not(df['PM_Nongzhanguan'][i] is np.nan):
            account[5][eval(df['month'][i])]+=int(df['PM_Nongzhanguan'][i])
            counters[5][eval(df['month'][i])]+=1   
        if not(df['PM_US Post'][i] is np.nan):
            account[5][eval(df['month'][i])]+=int(df['PM_US Post'][i])
            counters[5][eval(df['month'][i])]+=1

list_year=[]
month_trend=[0]*12
for i in range(6):
    sumt=0
    for j in range(1,13):
        print("year:{},month:{},meanIndex={:.2f}".format(i+2010,j,account[i][j]/counters[i][j]))
        sumt+=account[i][j]/counters[i][j]
        month_trend[j-1]+=account[i][j]/counters[i][j]
    print("year{}'s meanIndex={:.2f}".format(i+2010,sumt/12))
    list_year.append(round(sumt,2)/12)
print("Full process Time:",time.time()-start)

month=[1,2,3,4,5,6,7,8,9,10,11,12]
year=[2010,2011,2012,2013,2014,2015]
#调用plt.plot来画图,横轴纵轴两个参数即可
plt.plot(year,list_year)
plt.title=("Year Trend Graph")
# 用show展现出来图
plt.show()
plt.close()

plt.plot(month,month_trend)
plt.plot(month,month_trend)
plt.show()
