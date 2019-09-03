#%%
import numpy as np

#%%
# a.shape == b.shape 对应位做相应的运算
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

c = a*b
print(c)

#%%
# a b形状不同 自动触发broadcast
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])

b = np.array([1,2,3])

c = a * b
print(c)

#%% 原理解释

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])

b = np.array([1,2,3])
bb = np.tile(b,(4,1))

print(a+bb)

