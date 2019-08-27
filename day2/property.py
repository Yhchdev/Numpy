import numpy as np


#%%
# 输出维度
a = np.arange(24)
#print(a.ndim)

b = a.reshape(2,4,3)
print(b.ndim)


#%%
# shape 行 列
a = np.array([[1,2,3,4],[4,5,6,7]])
print(a.shape)
a.shape = (4,2)
print(a)

c = a.reshape(2,4)
print(c)