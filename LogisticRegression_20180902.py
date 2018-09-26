#-*- coding: utf-8 -*-
#逻辑回归 自动建模
# 如下可运用于根据特征来判断违约情况等

# # 如下可运用于根据特征来判断违约情况等
# import pandas as pd
#
# # 提取数据
# filename = 'bankloan.xls'
# data = pd.read_excel(filename)
# x = data.iloc[:,:8]
# y = data.iloc[:,8]
#
# # print (x)
# # print (y)
#
# from sklearn.linear_model import LogisticRegression as LR
# from sklearn.linear_model import RandomizedLogisticRegression as RLR
# rlr = RLR() #建立随机逻辑回归模型，筛选变量
# rlr.fit(x, y) #训练模型
# rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
# print(u'通过随机逻辑回归模型筛选特征结束。')
# # print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
# x = data[data.columns[rlr.get_support()]].as_matrix() #筛选好特征
#
# lr = LR() #建立逻辑货柜模型
# lr.fit(x, y) #用筛选后的特征数据来训练模型
# print(u'逻辑回归模型训练结束。')
# print(u'模型的平均正确率为：%s' % lr.score(x, y)) #给出模型的平均正确率，本例为81.4%




#-*- coding: utf-8 -*-
#逻辑回归 自动建模
# 如下可运用于根据特征来判断违约情况等

# # 如下可运用于根据特征来判断违约情况等
# import pandas as pd
#
# # 提取数据
# filename = 'bankloan.xls'
# data = pd.read_excel(filename)
# x = data.iloc[:,:8]
# y = data.iloc[:,8]
#
# # print (x)
# # print (y)
#
# from sklearn.linear_model import LogisticRegression as LR
# from sklearn.linear_model import RandomizedLogisticRegression as RLR
# rlr = RLR() #建立随机逻辑回归模型，筛选变量
# rlr.fit(x, y) #训练模型
# rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
# print(u'通过随机逻辑回归模型筛选特征结束。')
# # print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
# x = data[data.columns[rlr.get_support()]].as_matrix() #筛选好特征
#
# lr = LR() #建立逻辑货柜模型
# lr.fit(x, y) #用筛选后的特征数据来训练模型
# print(u'逻辑回归模型训练结束。')
# print(u'模型的平均正确率为：%s' % lr.score(x, y)) #给出模型的平均正确率，本例为81.4%




#-*- coding:utf8-8 -*-
# 20180926
# 逻辑回归 自动建模
import pandas as pd
from sklearn.utils import shuffle
#使用稳定性选择方法中的随机逻辑回归进行特征筛选，利用筛选后的特征建立逻辑回归模型，输出平均正确率
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
# filename='bankloan.xls'
# data=pd.read_excel(filename)  #返回值是DataFrame类型
# x=data.iloc[:,:8].as_matrix() #行全选，列选下标0-7
# y=data.iloc[:,8].as_matrix()  #行全选，列选下标8

# filename2='risk_train.xls'
# data=pd.read_excel(filename2)
# x=data.iloc[:,:30].as_matrix() #行全选，列选下标0-7
# y=data.iloc[:,30].as_matrix()  #行全选，列选下标8

filename3='model.xls'
data=pd.read_excel(filename3)
x=data.iloc[:,:3].as_matrix() #行全选，列选下标0-7
y=data.iloc[:,3].as_matrix()  #行全选，列选下标8


rlr=RLR()          #建立随机逻辑回归模型，筛选变量
rlr.fit(x,y)       #训练模型
rlr.get_support()  #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print('各个特征的分数:',rlr.scores_)
print ('通过随机逻辑回归模型筛选特征结束')
#打印的时候把2个东西连起来，用，逗号   java里面是+ 加号
#data.columns[rlr.get_support()]返回的是筛选后的列名,是一个迭代器
#S.join(iterable)  将iterable里面的元素用S连起来，S就是分隔符

#https://blog.csdn.net/pcy1127918/article/details/79975152
print('有效特征为:%s'% ','.join(data.columns[rlr.get_support(indices=True)]))
x=data[data.columns[rlr.get_support(indices=True)]].as_matrix()   #筛选好特征
lr=LR()               #建立逻辑货柜模型
lr.fit(x,y)           #用筛选后的特征数据来训练模型
print ('逻辑回归模型训练结束')
print ('模型的平均正确率为:',lr.score(x, y)) #给出模型的平均正确率，本例为81.4%


