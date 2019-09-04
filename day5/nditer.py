#%%
import numpy as np


#%%
a = np.arange(6).reshape(3,2)
print('原数组')
print(a)
print('\n')

print('迭代输出元素：')
for x in np.nditer(a):
    print(x,end=',')

#%%

print('迭代输出a的转置')
for x in np.nditer(a.T):
    print(x,end=',')


print('迭代输出以C顺序访问数组转置的copy')
for x in np.nditer(a.T.copy(order = "C")):
    print(x,end=',')



#%%

a = np.arange(0,60,5).reshape(3,4)
print('原始数组：')
print(a)
print('\n')

print('数组的转置：')
print(a.T)
print('\n')


# 以行的形式进行遍历
print('以C风格进行排序:')
b = a.copy(order='C')
print(b)

for x in np.nditer(b):
    print(x,end=",")

print('\n')


# 以 列的形式 遍历
print('以F风格进行排序：')
c = a.copy(order='F')
print(c)

for x in np.nditer(c):
    print(x,end=',')



#%%
# 修改值
a = np.arange(0,60,5)
a = a.reshape(3,4)
print("原数组")
print(a)
print('\n')

for x in np.nditer(a,op_flags = ['readwrite']):
    x[...] = 2 * x

print("修改后的数组：")
print(a)


#%%
# 使用外部loop
a = np.arange(0,60,5)
a = a.reshape(3,4)
print("原数组")
print(a)
print('\n')

# 按列遍历输出 flags
for x in np.nditer(a,flags = ['external_loop'],order= 'F'):
    print(x,end=',')



#%%
# 自动将小数组的形状 广播到大数组的形状
a = np.arange(0,60,5)
a = a.reshape(3,4)
print("第一个数组")
print(a)
print('\n')

b = np.array([1,2,3,4],dtype=int)
print('第二个数组')
print(b)
print('\n')

print('广播迭代后的数组:')
for x,y in np.nditer((a,b)):
    print('%d:%d' % (x,y),end = ',')





