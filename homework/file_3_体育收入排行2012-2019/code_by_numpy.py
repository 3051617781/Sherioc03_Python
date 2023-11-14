import numpy as np


# 读文件，数据类型统一设置为字符串，设置注释字符为None（避免#开头的数据被当作注释），读取时通过converters去除所有的#
sport_data = np.loadtxt('step3/2012-19sport.csv', str, delimiter=',', skiprows=1, comments=None,
                        converters={0: lambda x: x.strip('#')}, encoding='utf-8')
cmd = input()
if cmd.isdigit() and (2012 <= int(cmd) <= 2019):
    num = int(input())
    # 获取sport_data中最后一列（年份）值为cmd的前num行数据切片
    year_top_income = sport_data[sport_data[:, -1] == cmd][:num]
    # 列表推导式实现按格式循环输出
    [print(*item, sep=' | ') for item in year_top_income]
elif cmd.lower() == 'sport':
    year = input()
    # 获取sport_data中最后一列（年份）值为year的数据
    year_data = sport_data[sport_data[:, -1] == year]
    # 获取该年运动项目列表（按名称排序）
    year_sport_ls = sorted(set(year_data[:, -2]))
    # 构建该年运动项目菜单
    menu_data_dict = dict(zip(range(1, len(year_sport_ls) + 1), year_sport_ls))
    # 列表推导式输出菜单
    [print(f'{k}: {v}') for k, v in menu_data_dict.items()]
    # 输入运动项目编号
    # 构建该年运动项目菜单
    menu_data_dict = dict(zip(range(1, len(year_sport_ls) + 1), year_sport_ls))
    # 列表推导式输出菜单
    [print(f'{k}: {v}') for k, v in menu_data_dict.items()]
    # 输入运动项目编号
    num = int(input())
    # 取year_data中倒数第二列（运动项目）值为指定项目的数据
    result_data = year_data[year_data[:, -2] == menu_data_dict[num]]
    # 列表推导式实现按格式循环输出
    [print(*item, sep=' | ') for item in result_data]
    # 收入列去除$和M，转成浮点型
    income_data = np.char.replace(np.char.replace(result_data[:, 2], '$', ''), 'M', '').astype(float)
    # 计算并输出收入总和
    print(f'TOTAL: ${income_data.sum():.2f} M')
else:
    print('Wrong Input')
