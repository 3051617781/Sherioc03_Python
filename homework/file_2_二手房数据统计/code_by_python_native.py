with open('step2/house.csv', 'r', encoding='UTF-8') as f:
    house_title_ls = f.readline().strip().split(',')  # 首行拆分为标题列表
    house_data_ls = [line.strip().split(',') for line in f]  # 后续行通过列表推导式得到数据列表
n = input()
if n == '最高总价':
    t = int(input())
    # 对数据列表按总价降序排序后，截取前t名
    result_ls = sorted(house_data_ls, key=lambda x: eval(x[8]), reverse=True)[:t]
    print(*house_title_ls)  # 输出标题行，空格间隔
    [print(*i) for i in result_ls]  # 利用列表推导式，循环输出前t名的数据
elif n == '最大面积':
    t = int(input())
    # 对数据列表按面积降序排序后，截取前t名
    result_ls = sorted(house_data_ls, key=lambda x: eval(x[7]), reverse=True)[:t]
    print(*house_title_ls)  # 输出标题行，空格间隔
    [print(*i) for i in result_ls]  # 利用列表推导式，循环输出前t名的数据
elif n == '最高单价':
    # 对数据列表按单价（总价/面积）降序排序后，截取第一名
    result_ls = sorted(house_data_ls, key=lambda x: eval(x[8]) / eval(x[7]), reverse=True)[0]
    print(*house_title_ls)  # 输出标题行，空格间隔
    print(*result_ls)  # 输出前1名的数据
elif n == '精装电梯房单价':
    # 列表推导式，获取所有精装电梯房的面积和总价，构成二维列表
    result_ls = [[eval(i[7]), eval(i[8])] for i in house_data_ls if i[6] == '有电梯' and i[5] == '精装']
    # 列表推导式分别获取总价列表和面积列表，两个列表分别求和后做除法，即为精装电梯房单价
    print(f'{sum([i[1] for i in result_ls]) / sum([i[0] for i in result_ls]):.2f}万元')
elif n == '房屋朝向':
    s = input()
    # 列表推导式，获取所有朝向为输入值s的房屋数据列表
    result_ls = [i for i in house_data_ls if i[3] == s]
    # 条件表达式，根据结果列表长度是否为0，输出不同内容
    print(f'{len(result_ls)}套') if len(result_ls) != 0 else print('无数据')
else:
    # 列表推导式，获取所有小区名中包含n的房屋数据列表
    result_ls = [i for i in house_data_ls if n in i[1]]
    print(*house_title_ls)  # 输出标题行，空格间隔
    # 条件表达式，根据结果列表长度是否为0，输出不同内容。不为0时，利用列表推导式，循环输出结果列表的数据
    print('未找到相关数据') if len(result_ls) == 0 else [print(*i) for i in result_ls]
