# -*- coding: utf-8 -*-
'''
DataFrame的CRUD
'''
import pandas as pd

master = pd.read_csv("pandas_3/Training_Master.csv",encoding='gbk')
user = pd.read_csv("pandas_3/Training_Userupdate.csv",encoding='gbk')
log = pd.read_csv("pandas_3/Training_LogInfo.csv",encoding='gbk')

#	2.1 求取master表的列名前缀列表，并按字母升序输出该列表。
#     例如：SocialNetwork_12列的列名前缀为：SocialNetwork
############begin############





#############end#############

#	2.2 删除master中列名前缀为：SocialNetwork的列
#     输出：共**列被删除。
############begin############






#############end#############

#	2.3在master表最右侧增加一列Result，
#    记录UserInfo_1和UserInfo_3的和，
#    并输出这三列的前5行。
############begin############



#############end#############

#	2.4将UserInfo_2列中所有的“深圳”替换为“中国深圳”，
#    并计算“中国深圳”的用户数。
############begin############



#############end#############