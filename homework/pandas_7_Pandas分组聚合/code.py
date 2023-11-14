import pandas as pd
import numpy as np


def sub(df):
    """
    返回df中最大值与最小值的差
    """
    # ####### Begin #######
    return df.max() - df.min()
    # ####### End #######


def main():
    """
    利用groupby、agg、统计函数和自定义函数sub，求每个大洲红酒消耗量的最大值与最小值的差以及啤酒消耗量的和
    """
    # ####### Begin #######
    data = pd.read_csv("pandas_7/drinks.csv")
    df = pd.DataFrame(data)
    mapping = {"wine_servings": sub, "beer_servings": np.sum}  # 建立列名与对应处理函数的字典
    print(df.groupby("continent").agg(mapping))
    # ####### End #######


if __name__ == '__main__':
    main()