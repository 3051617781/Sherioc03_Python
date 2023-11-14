# -*- coding: utf-8 -*-
"""
数据清洗
"""
import pandas as pd

ChinaData = pd.read_csv('pandas_6_数据清洗/pandas_6/ChinaData.csv', index_col=0)
"""
请针对ChinaData完成如下操作。
"""
# 2.1 按如下格式输出删除前ChinaData的形状
# 格式：原表形状(x, y)
# ###########begin############
before_shape = ChinaData.shape
print('原表形状'+str(before_shape))
# ############end#############
# 2.2 直接删除ChinaData的空白行
# 提示：dropna,inplace
# ###########begin############
ChinaData.dropna(how='all', inplace=True)
# ############end#############
# 2.3 按如下格式输出删除后ChinaData的形状
# 格式：新表形状(x, y)
# ###########begin############
after_shape = ChinaData.shape
print('新表形状'+str(after_shape))
# ############end#############
# 2.4 按如下格式输出被删除的空行数
# 格式：XX个空白行被删除。
# ###########begin############
print(f"{before_shape[0]-after_shape[0]}个空白行被删除。")
# ############end#############
# 2.5 查找数据最完整（空值最少）的年份并输出
# 提示：notnull(),根据值找索引
# ###########begin############
nullsummary = ChinaData.isnull().sum()
print(nullsummary.loc[nullsummary == nullsummary.min()].index[0])
# ############end#############
# 2.6 前向填充"男性吸烟率（吸烟男性占所有成年人比例）"，输出2000年至2019年的数据
# fillna,ffill
# ###########begin############
cigarette = ChinaData.loc['男性吸烟率（吸烟男性占所有成年人比例）', :]
print(cigarette.fillna(method='ffill').loc['2000':'2019'])
# ############end#############
