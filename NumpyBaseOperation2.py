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
print(np.median(A))

#累加函数
print(np.cumsum(A))

#累差运算函数 该函数计算的便是每一行中后一项与前一项之差
print(np.diff(A))

#nonzero()函数 这个函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。
print(np.nonzero(A))

#矩阵转秩
print(np.transpose(A))
print(A.T)

#clip函数  clip(Array,Array_min,Array_max)
print(np.clip(A,5,9))