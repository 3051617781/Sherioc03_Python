import pandas as pd


def task3():
    # ********** Begin **********#
    # 读取三个csv文件
    pop = pd.read_csv("pandas_9/state-population.csv")
    areas = pd.read_csv("pandas_9/state-areas.csv")
    abbrevs = pd.read_csv("pandas_9/state-abbrevs.csv")
    # 合并pop和abbrevs并删除重复列
    merged = pd.merge(pop, abbrevs, how="outer", left_on="state/region", right_on="abbreviation")
    merged = merged.drop('abbreviation', axis=1)
    # 填充对应的全称
    merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
    merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
    # 合并面积数据
    final = pd.merge(merged, areas, on='state', how='left')
    # 删掉这些缺失值
    final.dropna(inplace=True)
    # 取year为2010年的数据，并将索引设为state列
    data2010 = final[final["year"] == 2010]
    data2010.set_index("state", inplace=True)
    # 计算人口密度
    density = data2010['population'] / data2010['area (sq. mi)']
    # 对密度求和
    get_sum = density.groupby("state").sum()
    # 对值进行排序
    result = get_sum.sort_values(ascending=False)
    # 输出人口密度前5名和倒数5名
    print(f"前5名：\n{result.head()}")
    print(f"后5名：\n{result.tail()}")
    # ********** End **********#
