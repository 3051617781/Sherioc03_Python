import pandas as pd

# 读文件，读取时通过converters去除所有的#
sport_data = pd.read_csv('step3/2012-19sport.csv', converters={'Rank': lambda x: x.strip('#')}, encoding='utf-8')
cmd = input()
if cmd.isdigit() and (2012 <= int(cmd) <= 2019):
    num = int(input())
    # 获取sport_data中year列值为cmd的前num行数据切片
    year_top_n_data = sport_data[sport_data['Year'] == int(cmd)][:num]
    # 列表推导式实现按格式循环输出
    [print(*item, sep=' | ') for item in year_top_n_data.values]
elif cmd.lower() == 'sport':
    year = int(input())
    # 获取sport_data中year列值为year的数据
    year_data = sport_data[sport_data['Year'] == year]
    # 获取该年运动项目列表（按名称排序）
    year_sport_ls = sorted(year_data['Sport'].unique())
    # 构建该年运动项目菜单
    menu_data_dict = dict(zip(range(1, len(year_sport_ls) + 1), year_sport_ls))
    # 列表推导式输出菜单
    [print(f'{k}: {v}') for k, v in menu_data_dict.items()]
    # 输入运动项目编号
    num = int(input())
    # 取year_data中sport列值为指定项目的数据
    result_data = year_data[year_data['Sport'] == menu_data_dict[num]]
    # 列表推导式实现按格式循环输出
    [print(*item, sep=' | ') for item in result_data.values]
    # pay列切片去除$和M，转成浮点型
    income_data = result_data['Pay'].str[1:-2].astype('float')
    # 计算并输出收入总和
    print(f'TOTAL: ${income_data.sum():.2f} M')
else:
    print('Wrong Input')
