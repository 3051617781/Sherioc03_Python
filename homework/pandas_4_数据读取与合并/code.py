# -*- coding: utf-8 -*-
"""
第1关 数据读取与合并
现有源自世界银行的四个数据集：
1)economy-60-78.csv，
2)economy-79-19.csv，
3)population-60-78.csv，
4)population-79-19.csv，
其中分别存放了不同时间段（1960-1978和1979-2019）的
中国经济相关数据和中国人口及教育相关数据。
"""
# 请将上述数据集内容读取至DataFrame结构中，
# 年份为列索引，Indicator Name为行索引，
# 观察其结构和内容，把它们合并为一个DataFrame，命名为ChinaData。
# 输出ChinaData的形状
# ###########begin############
import pandas as pd

d1 = pd.read_csv('pandas_4/economy-60-78.csv', index_col=0)
d2 = pd.read_csv('pandas_4/economy-79-19.csv', index_col=0)
d3 = pd.read_csv('pandas_4/population-60-78.csv', index_col=0)
d4 = pd.read_csv('pandas_4/population-79-19.csv', index_col=0)
d12 = pd.concat([d1, d2], axis=1, sort=True)
d34 = pd.concat([d3, d4], axis=1, sort=True)
ChinaData = pd.concat([d34, d12], sort=True)
print(ChinaData.shape)
# ############end#############
