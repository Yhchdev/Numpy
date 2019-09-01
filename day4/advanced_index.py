#%%
import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
# 获取（0,1）(2,0)位置处的元素
y = x[[0,2],[1,0]]

print(y)

#%%
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')

# 4个角个行索引
rows = [[0,0],[3,3]]
# 4个角的列索引
cols = [[0,2],[0,2]]
y = x[rows,cols]
print("这个数组的四个角的元素是：")
print(y)

#%%

a = np.array([[1,2,3], [4,5,6],[7,8,9]])
# 行（1,2）行,列(1,2) 列
b = a[1:3,1:3]
print(b)

c = a[1:3,[1,2]]
print(c)

# ... : 组合使用
d = a[...,2:]
print(d)

#%%
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print  ('大于 5 的元素是：')
print(x>5)

print(x[x>5])

#%%

# 通过 ~（取补运算）来过滤掉一些元素

a = np.array([np.nan, 1, 2, 3, np.nan, 4, 5])

print(a[~np.isnan(a)])

#%%
# 过滤掉非负数

a = np.array([1,  2+6j,  5,  3.5+5j])

print(a[~np.iscomplex(a)])

#%%

a = np.arange(32).reshape((8,4))
print(a)
# 获取第4行，2行，1行，7行
print(a[[4,2,1,7]])

# 倒序
print('\n')
print('按倒序输出：')
print(a[[-4,-2,-1,-7]])

# 传入多个索引数组

#%%
x = np.arange(32).reshape(8,4)
print(x)

print(x[np.ix_([1,5,7,2],[0,3,1,2])])


