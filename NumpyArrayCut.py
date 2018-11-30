#coding:utf-8
import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

#纵向分割   等分为n块
print(np.split(A,2,axis=1))

#横向分割
print(np.split(A,3,axis=0))

#不等分切割
print(np.array_split(A,3,axis=1))
