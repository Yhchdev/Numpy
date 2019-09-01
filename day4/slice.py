#%%
import numpy as np


#%%
a = np.arange(10)
s = slice(2,7,2)
print(a[s])

#%%
print(a[2:7:2])

#%% index
print(a[5])
print(a[5:])
print(a[2:7])

#%% 多维数组
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(b[1:])
# 省略行,取第0列
print(b[...,0])
print(b[...,1])

# 省略列，取第二列
print(b[2,...])
# 取第二，三行余下的
print(b[1:,...])


