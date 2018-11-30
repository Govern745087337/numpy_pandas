#coding:utf-8
import numpy as np

A = np.ones((1,3))[0]
B = np.array([2,2,2])

print(A)
print(B)

#合并数组
print(np.vstack((A,B)))   # vertical stack

print(np.hstack((A,B)))   # horizontal stack


A = np.ones((1,3))
B = np.zeros((1,3))
C = np.concatenate((A,B,B,A),axis=0)
print(C)

D = np.concatenate((A,B,B,A),axis=1)
print(D)