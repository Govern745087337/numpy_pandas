#coding:utf-8
import numpy as np

A = np.arange(2,14).reshape((3,4))
print(A)

# argmin() 和 argmax() 两个函数分别对应着求矩阵中最小元素和最大元素的索引
print(np.argmin(A))
print(np.argmax(A))

#求均值
print(np.mean(A))
print(np.average(A))

#求中位数的函数
print(np.median())


