import numpy as np

# 创建数组

#%%
#1.底层 ndarry 构造器

a = np.array([[1,2,3],[4,5,6]])
print(a)

#%%
# empty 未初始化 随机值
b  = np.empty((3,2),dtype=int)
print(b)

#%%

x = np.zeros([3,2],dtype=int)
print(x)