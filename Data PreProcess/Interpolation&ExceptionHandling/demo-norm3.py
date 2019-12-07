import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[11,12])

#生成fig对象和ax对象
fig = plt.figure()
ax1 = fig.add_subplot(131) #表示共有3个子图，1行3列布局，ax1是第1个子图

#子图1：原始图像
x = df["PRES_new2"]
y = df["HUMI_new2"]
ax1.scatter(x, y, s=10)  #x和y分布是点的x和y坐标，s为散点的大小
#ax1.set_xlim(0,1250)   #设置x轴刻度的最大最小值
#ax1.set_ylim(0,120)    #设置y轴刻度的最大最小值
ax1.set_title("Original")  #设置标题

#子图2:(0,1)归一化，采用MinMaxScaler函数
ax2 = fig.add_subplot(132) #表示共有3个子图，1行3列布局，ax2是第2个子图

#子图3:Z-score归一化，采用StandardScaler函数
ax3 = fig.add_subplot(133) #表示共有3个子图，1行3列布局，ax3是第3个子图

#显示图形
plt.show()


