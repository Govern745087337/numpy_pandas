#coding:utf-8
"""
array：创建数组
dtype：指定数据类型
zeros：创建数据全为0
ones：创建数据全为1
empty：创建数据接近0
arrange：按指定范围创建数据
linspace：创建线段
创建数组
"""
import numpy as np

a = np.array([2,23,4])
print(a)

#指定数据类型
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)

a = np.array([2,23,4],dtype=np.int64)
print(a.dtype)

a = np.array([2,23,4],dtype=np.float)
print(a.dtype)

a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)

#创建特定数据类型
a = np.array([[2,23,4],[2,23,4]]) #2d矩阵 2行3列
print(a)

#创建全零数组
a = np.zeros((3,4)) #数据全为0，3行4列
print(a)

#创建全1数组 也可以指定dtype
a = np.ones((3,4),dtype=(np.int64))
print(a)

#创建全空数组 每个值都接近于0
a = np.empty((3,4),dtype=np.float)
print(a)

#使用reshape改变数据的形状
a = np.arange(12).reshape((3,4))
print(a)

#使用linspace创建线段型数组
a = np.linspace(1,10,20).reshape((4,5))  #开始1 结束10 分成20个数据
print(a)