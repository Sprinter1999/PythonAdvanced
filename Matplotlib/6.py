import matplotlib.pyplot as plt
import pandas as pd
fig,ax=plt.subplots()
# 读取数据
iris = pd.read_csv( 'iris.csv')
colors = [ 'r', 'y', 'b'] # 定义三种散点的颜色
Species = iris.Species.unique() #对类别去重
plt.subplot(4,4,1) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'], iris.loc[iris.Species== Species[i], 'Petal.Width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Length vs Width')
plt.xlabel( 'Petal.Length')
plt.ylabel( 'Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,2) #设置子图有2个，即1行2列，再画右边的第二个
for i in range(len(Species)): #x和y轴交换一下位置
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Width'], iris.loc[iris.Species== Species[i], 'Petal.Length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Width vs Length')
plt.xlabel( 'Petal.Width')
plt.ylabel( 'Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例
plt.show()

plt.subplot(4,4,3) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.length'], iris.loc[iris.Species== Species[i], 'Petal.Width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'length vs Width')
plt.xlabel( 'Sepal.Length')
plt.ylabel( 'Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,4) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Width'], iris.loc[iris.Species== Species[i], 'Sepal.length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Width vs length')
plt.xlabel( 'Petal.Width')
plt.ylabel( 'Sepal Length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,5) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.width'], iris.loc[iris.Species== Species[i], 'Sepal.width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'width vs width')
plt.xlabel( 'Sepal.width')
plt.ylabel( 'Setal.width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,6) #设置子图有2个，即1行2列，再画右边的第二个
for i in range(len(Species)): #x和y轴交换一下位置
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'], iris.loc[iris.Species== Species[i], 'Petal.Length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Length vs Length')
plt.xlabel( 'Petal.Length')
plt.ylabel( 'Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例
plt.show()

plt.subplot(4,4,7) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Width'], iris.loc[iris.Species== Species[i], 'Petal.Width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Width vs Width')
plt.xlabel( 'Pedal Width')
plt.ylabel( 'Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,8) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.length'], iris.loc[iris.Species== Species[i], 'Sepal.length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'length vs length')
plt.xlabel( 'Sepal.length')
plt.ylabel( 'Sepal.length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,9) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.length'], iris.loc[iris.Species== Species[i], 'Sepal.width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'length vs width')
plt.xlabel( 'Sepal.length')
plt.ylabel( 'Sepal.width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,10) #设置子图有2个，即1行2列，再画右边的第二个
for i in range(len(Species)): #x和y轴交换一下位置
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.width'], iris.loc[iris.Species== Species[i], 'Sepal.length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'width vs length')
plt.xlabel( 'Sepal.width')
plt.ylabel( 'Sepal.length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例
plt.show()

plt.subplot(4,4,11) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.length'], iris.loc[iris.Species== Species[i], 'Petal.Length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'length vs Length')
plt.xlabel( 'Sepal.length')
plt.ylabel( 'Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,12) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'], iris.loc[iris.Species== Species[i], 'Sepal.length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Length vs length')
plt.xlabel( 'Petal.Length')
plt.ylabel( 'Sepal length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,13) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'], iris.loc[iris.Species== Species[i], 'Sepal.width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Length vs width')
plt.xlabel( 'Petal.Length')
plt.ylabel( 'Sepal.width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,14) #设置子图有2个，即1行2列，再画右边的第二个
for i in range(len(Species)): #x和y轴交换一下位置
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.width'], iris.loc[iris.Species== Species[i], 'Petal.Length'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'width vs Length')
plt.xlabel( 'Sepal.width')
plt.ylabel( 'Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例
plt.show()

plt.subplot(4,4,15) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Sepal.width'], iris.loc[iris.Species== Species[i], 'Petal.Width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'width vsWidth')
plt.xlabel( 'Sepal.width')
plt.ylabel( 'Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例

plt.subplot(4,4,16) #设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Width'], iris.loc[iris.Species== Species[i], 'Sepal.width'], s = 20, c = colors[i], label = Species[i])
# 添加轴标签和标题
plt.title( 'Width vs width')
plt.xlabel( 'Petal.Width')
plt.ylabel( 'Sepal width')
plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
# plt.legend(loc = 'lower right') # 添加图例