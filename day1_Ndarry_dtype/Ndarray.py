import numpy as np

#%% 一维
a = np.array([1,2,3])
print(a)

#%% 二维
b = np.array(
    [ [1,2,3],
      [4,5,6] ]
    )
print(b)


#%% ndmin 指定生成数组的最小维度
c = np.array([1,2,3,4,5],ndmin=3)
print(c)

#%% dtype 指定数组元素的数据类型

e = np.array([1,2,3], dtype= complex)
print(e)



