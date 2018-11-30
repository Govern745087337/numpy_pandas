#coding:utf-8
import numpy as np

"""数据具有关联性"""
a = np.arange(4)
print(a)

b=a
c=b
d=c

d[1:3] = [22,33]
print(a)

"""数据取消关联性的方式"""
a = np.arange(4)
b = a.copy()
print(b)
a[3]=9
print(a)
print(b)

