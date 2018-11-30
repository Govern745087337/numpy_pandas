#coding:utf-8
import numpy as np

A = np.arange(3,15)

print(A[3])

A = np.arange(3,15).reshape((3,4))
print(A)
print(A[0])

print(A[1][1])
print(A[1,1])

#数组切片
print(A[:,2:4])

#数组展平输出
print(A.flatten())
print(A.reshape(1,A.size)[0])