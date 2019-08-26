import numpy as np

#%% 指定数据类型
dt = np.dtype(np.int32)
print(dt)

#%%

dt = np.dtype([('age',np.int8)])
print(dt)

#%% 将数据类型应用于 ndarry 对象
dt = np.dtype([('age',np.int8)])
a = np.array([(20),(21),(22)],dtype=dt)

print(a)
#类型字段名可用于存取实际的age列
print(a['age'])

#%%
student = np.dtype([('name','S20'),('age','i1'),('mark','f4')])
a = np.array([('qq',22,99),('yhchdev',20,88),('yhch',19,66)],dtype=student)
print(a)