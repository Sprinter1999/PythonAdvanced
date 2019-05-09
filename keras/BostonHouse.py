#!/usr/bin/env python
# coding: utf-8

# # Boston House Predicate

# In[1]:


#TODO：
'''
The dataframe has 506 rows and 14 columns.And data refers to crime,rooms,nox(Nitrogen index),etc
And our goal is to predict Boston house price MEDV（中位数）

And our scoring is based on RMSE.
'''


# In[3]:


import keras
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
import numpy as np


# In[4]:


(train_data,train_target),(test_data,test_target)=boston_housing.load_data()


# In[5]:


train_data.shape


# In[6]:


test_data.shape


# In[9]:


train_target #先看一眼，大概结果是如下结果，单位是 千美元


# 由概率论知识，我们进行标准化处理：$X_t =\frac{X-mean}{std}$

# In[8]:


mean=train_data.mean(axis=0)#按照列维度取均值
std=train_data.std(axis=0)

train_data=(train_data-mean)/std
test_data=(test_data-mean)/std


# ## 数据预处理到此为止，之后我们构造神经网络，从中可以发现：
# ### 数据量较小，非常容易过拟合，所以我们模型不应该太复杂，用两个隐藏层即可

# In[11]:


def build_model():
    model=Sequential()
    model.add(Dense(64,input_shape=(13,),activation='relu'))
    model.add(Dense(64,activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer=RMSprop(),loss="mse",metrics=["mae"])
    #因为题目要求的方式是RMSE,mae平方绝对误差
    return model
    


# ## 众所周知，当数据较小的时候，我们应该采取交叉验证

# <img src="imgs/cross_val.png">
# <h3>一般而言，我们Fold取10 or 5,当得到的结果的平均水平我们可以接受了，再用所有的数据作为训练集
# <h3>构造一个模型，再对test集进行检验

# In[12]:


k=4#(emmm,train data we have 404)
num_val_samples=len(train_data)//k #(Python3)
num_epochs=100
all_scores=[]


# In[17]:


for i in range(k):
    val_data=train_data[i*num_val_samples:(i+1)*num_val_samples]
    val_targets=train_target[i*num_val_samples:(i+1)*num_val_samples]
    
    partial_train_data=np.concatenate(
                                      [train_data[:i*num_val_samples],
                                      train_data[(i+1)*num_val_samples:]],
                                      axis=0
                                     )
    partial_train_targets=np.concatenate(
                                    [train_target[:i*num_val_samples],
                                      train_target[(i+1)*num_val_samples:]],
                                      axis=0
                                     )
    
    model =build_model()
    model.fit(partial_train_data,partial_train_targets,epochs=num_epochs,batch_size=1,verbose=0)
     
    val_mse,val_mae=model.evaluate(val_data,val_targets,verbose=0)
    
    all_scores.append(val_mae)
    print("第","i+1","Fold的MSE：",val_mse,"MAE:",val_mae)


# In[18]:


np.mean(all_scores)


# In[20]:


model=build_model()
model.fit(train_data,train_target,epochs=80,batch_size=16,verbose=0)


# In[21]:


test_mse,test_mae=model.evaluate(test_data,test_target)


# In[22]:


test_mse


# In[23]:


np.sqrt(test_mse)


# #### 比较上面的结果和Kaggle上的排名，训练效果还是可以，能在30%以内，再继续优化的话可能需要在特征工程上做做功课了
