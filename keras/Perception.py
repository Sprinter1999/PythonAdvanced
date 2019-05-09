#@LINK:A hyperplane in Rn is an n-1 dimensional subspace
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#中文标签
plt.rcParams['axes.unicode_minus']=False#正常显示负号
plt.rcParams['figure.figsize']=(8,6)#figsize

    #TODO:Randomly generate 100 points
fig=plt.figure()
    #figa=plt.gca()#get current canvas

N=100
xn=np.random.rand(N,2)
x=np.linspace(0,1)#0,1之间平均的产生50个点（默认参数）

    #randomly generate a line
a=np.random.rand()
b=np.random.rand()
f=lambda x:a*x+b
plt.plot(x,f(x),'r')

    #linearly cut those points
yn=np.zeros([N,1])

for i in range(N):
    if(f(xn[i,0])>=xn[i,1]):
            #point is below line
        yn[i]=1
        plt.plot(xn[i,0],xn[i,1],'bo',markersize=12)
    else:
            #else
        yn[i]=-1
        plt.plot(xn[i,0],xn[i,1],'go',markersize=12)
# plt.legend(['Cut Line','Class1','Class2'],loc=2)
# plt.title("Random Number Generating and Plot")

def perception(xn,yn,MaxIter=1000,a=0.1,w=np.zeros(3)):
    '''
    For a 2-dim perception :
    对于一个给定的（X，Y），感知机将会迭代寻找最佳的超平面进行分类
    输入：
    xn 数据点 N*2 vector
    yn 分类结果 N*1 vector
    MaxIter：迭代次数
    a：learning rate
    w：Initial arguments

    输出：
    w：较好的超平面参数

    说明：
    只是简单实现而已
    '''
    N=xn.shape[0]
    #Forward
    f=lambda x:np.sign(w[0]*1+w[1]*x[0]+w[2]*x[1])
    #Backward
    for _ in range(MaxIter):
        i=np.random.randint(N)

        if(yn[i]!=f(xn[i,:])):
            w[0]=w[0]+yn[i]*1*a
            w[1]=w[1]+yn[i]*xn[i,0]*a
            w[2]=w[2]+yn[i]*xn[i,1]*a
        
        return w
    
w=perception(xn,yn)
#利用w计算y=ax+b的ab
bnew=-w[0]/w[2]
anew=-w[1]/w[2]
y=lambda x:anew*x+bnew

sep_color=(yn)/2.0
plt.figure()
figa=plt.gca()

plt.scatter(xn[:,0],xn[:,1],c=sep_color.flatten(),s=50)
plt.plot(x,y(x),'b-',label="Perception classification")
plt.plot(x,f(x),'r',label="原始分类曲线")
plt.legend()
plt.title("原始曲线与Perception比较")
plt.show()