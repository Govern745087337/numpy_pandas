import pandas as pd
import numpy as np

#创建一个序列
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

#创建一个数据帧
dates = pd.date_range('20160102',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
"""
                   a         b         c         d
2016-01-02 -0.546266  1.204452 -1.548371 -0.751911
2016-01-03  0.660693 -2.241263  1.100281  0.875308
2016-01-04  0.487297  0.815907  0.256840 -0.116047
2016-01-05 -0.630754  0.457750  0.969650 -0.634060
2016-01-06  0.115383 -0.106663 -0.757858 -0.001741
2016-01-07  0.914717 -0.840165 -0.710883  1.787914
"""
print(df['b'])
"""
2016-01-02    3.336844
2016-01-03    1.454235
2016-01-04    0.389815
2016-01-05    0.267486
2016-01-06   -1.098787
2016-01-07   -1.243390
Freq: D, Name: b, dtype: float64
"""
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
print(df2.dtypes)
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""
print(df2.index)
"""
Int64Index([0, 1, 2, 3], dtype='int64')
"""
print(df2.columns)
"""
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
"""
print(df2.values)
"""
[[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
"""
print(df2.describe())
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""
print(df2.T)   #转秩
print(df2.sort_index(axis=1, ascending=False))  #对数据的 index 进行排序并输出
print(df2.sort_values(by='B'))   #对数据 值 排序输出
