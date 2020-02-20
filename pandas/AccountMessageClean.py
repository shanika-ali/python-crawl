# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame

# index_col=0 读取excel时，忽略最左侧
data = pd.read_excel('/data/www/python-crawl/pandas/accountMessage.xlsx', index_col=0, encoding='utf-8')
df = DataFrame(data)

# 重命名列名
new_col = ['Num', 'Name', 'Age', 'Weight', 'm1', 'm2', 'm3', 'f1', 'f2', 'f3']
df.columns = new_col

# 删除全空行
df.dropna(how='all', inplace=True)

# 均值填充Age, 并取整
df['Age'].fillna(round(df['Age'].mean()), inplace=True)

# 高频值填充f2
age_maxf = df['f2'].value_counts().index[0]
df['f2'].fillna(age_maxf, inplace=True)

# 获取 weight 数据列中单位为 lbs 的数据
rows_with_lbs = df['Weight'].str.contains('lbs').fillna(False)
# 将 lbs转换为 kgs, 2.2lbs=1kgs
for i, lbs_row in df[rows_with_lbs].iterrows():
  # 截取从头开始到倒数第三个字符之前，即去掉lbs。
  weight = int(float(lbs_row['Weight'][: -3]) / 2.2)
  df.at[i, 'Weight'] = '{}kgs'.format(weight)

# 高频值填充weight
weight_maxf = df['Weight'].value_counts().index[0]
df['Weight'].fillna(weight_maxf, inplace = True)

# 拆分name列, split的第二个参数表示将分列结果转换为DataFrame
df['FirstName'], df['LastName'] = df['Name'].str.split(' ', True).str

# 删除原Name列
df.drop(['Name'], axis = 1, inplace=True)

# 移动first_name和last_name这俩列
first_name = df.pop('FirstName')
df.insert(1,'FirstName',first_name)
last_name = df.pop('LastName')
df.insert(2,'LastName',last_name)

print(df)

