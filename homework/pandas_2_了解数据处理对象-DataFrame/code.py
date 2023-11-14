# -*- coding: utf-8 -*-
import pandas as pd


def create_dataframe():
    """
    返回值:
    df1: 一个DataFrame类型数据
    """
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    dictionary = {'states': [1, 1, 1, 1, 1], 'pops': [2, 2, 2, 2, 2], 'years': [3, 3, 3, 3, 3]}
    df1 = pd.DataFrame(dictionary, index=['one', 'two', 'three', 'four', 'five'])
    df1['new_add'] = [7, 4, 5, 8, 2]
    # ********** End **********#

    # 返回df1
    return df1
