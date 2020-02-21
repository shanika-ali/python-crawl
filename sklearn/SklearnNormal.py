# -*- coding: utf-8 -*-
# 采用sklearn进行数据归一化

from sklearn import preprocessing
import numpy as np

# 初始化数据
x = np.array([[ 0, -3,  1],
              [ 3,  1,  2],
              [ 0,  1, -1]])

# 将数据进行[0,1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)


# 将数据进行Z-Score规范化
scaled_x = preprocessing.scale(x)
print(scaled_x)

# 小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)


# test
x = np.array([[5000],[58000],[16000]])
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)