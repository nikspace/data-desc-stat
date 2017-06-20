# -*- coding: utf-8 -*- 
from numpy import array
from numpy.random import normal, randint

from numpy import mean,median
from numpy import mean, ptp, var, std
from numpy import array, cov, corrcoef

#使用List来创造一组数据
data = [1, 2, 3]
#使用ndarray来创造一组数据
data = array([1, 2, 3])
#创造一组服从正态分布的定量数据
data = normal(0, 10, size=10)
#创造一组服从均匀分布的定性数据
data = randint(0, 10, size=10)

#---中心位置（均值、中位数、众数）
#计算均值
print mean(data)
#计算中位数
print median(data)

#--发散程度（极差、方差、标准差、变异系数）
#极差
ptp(data)
#方差
var(data)
#标准差
std(data)
#变异系数
mean(data) / std(data)

#---偏差程度
#计算第一个值的z-分数
(data[0]-mean(data)) / std(data)

#--相关程度

data = array([data1, data2])

#计算两组数的协方差
#参数bias=1表示结果需要除以N，否则只计算了分子部分
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的协方差。对角线为方差
cov(data, bias=1)

#计算两组数的相关系数
#返回结果为矩阵，第i行第j列的数据表示第i组数与第j组数的相关系数。对角线为1
corrcoef(data)
