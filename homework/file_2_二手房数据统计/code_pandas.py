import pandas as pd

# 数据以字符串读入，避免输出格式错误
house_df = pd.read_csv('step2/house.csv', delimiter=',', dtype=str, encoding='utf-8')
# 添加三列，用于排序
house_df['面积'] = house_df['面积(㎡)'].astype(float)
house_df['总价'] = house_df['价格(万元)'].astype(float)
house_df['单价'] = house_df['总价']/house_df['面积']
n = input()
if n == '最高总价':
    t = int(input())
    # 对DataFrame按总价降序排序后，截取前t名
    result_df = house_df.sort_values(by='总价', axis=0, kind='stable', ascending=False)[:t]
    print(*house_df.columns[:10])  # 输出标题行，空格间隔，去除为排序自行添加的
    [print(*i) for i in result_df.loc[:, '市区':'年份'].values]  # 利用列表推导式，循环输出前t名的数据，去除为排序自行添加的
elif n == '最大面积':
    t = int(input())
    # 对DataFrame按面积降序排序后，截取前t名
    result_df = house_df.sort_values(by='面积', axis=0, kind='stable', ascending=False)[:t]
    print(*house_df.columns[:10])  # 输出标题行，空格间隔，去除为排序自行添加的
    [print(*i) for i in result_df.loc[:, '市区':'年份'].values]  # 利用列表推导式，循环输出前t名的数据，去除为排序自行添加的
elif n == '最高单价':
    # 对DataFrame按单价降序排序后，重新编号后截取第一名
    result_df = house_df.sort_values(by='单价', axis=0, kind='stable', ascending=False).reset_index(drop=True)
    print(*house_df.columns[:10])  # 输出标题行，空格间隔，去除为排序自行添加的
    print(*result_df.loc[0, '市区':'年份'].values)  # 输出，去除为排序自行添加的
elif n == '精装电梯房单价':
    # 构建筛选条件
    filter_criteria = ('有电梯' == house_df['电梯']) & (house_df['装修情况'] == '精装')
    # 条件删选获得所有精装电梯房的数据，得到新数组
    result_df = house_df[filter_criteria]
    # 计算精装电梯房单价
    print(f"{result_df['总价'].sum()/result_df['面积'].sum():.2f}万元")
elif n == '房屋朝向':
    s = input()
    # 获取朝向为输入值s的个数
    result_count = (s == house_df['朝向']).sum()
    # 条件表达式，根据结果列表长度是否为0，输出不同内容
    print(f'{result_count}套') if result_count != 0 else print('无数据')
else:
    # 判断那些行小区名中包含n，返回布尔数组
    filter_df = house_df['小区'].str.contains(n)
    print(*house_df.columns[:10])  # 输出标题行，空格间隔，去除为排序自行添加的
    # 条件表达式，根据结果长度是否为0，输出不同内容。不为0时，利用列表推导式，循环输出结果数据
    print('未找到相关数据') if filter_df.sum() == 0 else [print(*i) for i in house_df[filter_df].loc[:, '市区':'年份'].values]
