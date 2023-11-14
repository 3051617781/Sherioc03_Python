import numpy as np

house_array = np.loadtxt('step2/house.csv', delimiter=',', dtype=str, encoding='utf-8')
n = input()
if n == '最高总价':
    t = int(input())
    # 对数组按总价降序排序后，截取前t名
    result_ls = sorted(house_array[1:], key=lambda x: eval(x[8]), reverse=True)[:t]
    print(*house_array[0])  # 输出标题行，空格间隔
    [print(*i) for i in result_ls]  # 利用列表推导式，循环输出前t名的数据
elif n == '最大面积':
    t = int(input())
    # 对数组按面积降序排序后，截取前t名
    result_ls = sorted(house_array[1:], key=lambda x: eval(x[7]), reverse=True)[:t]
    print(*house_array[0])  # 输出标题行，空格间隔
    [print(*i) for i in result_ls]  # 利用列表推导式，循环输出前t名的数据
elif n == '最高单价':
    # 对数组按单价（总价/面积）降序排序后，截取第一名
    result_ls = sorted(house_array[1:], key=lambda x: eval(x[8]) / eval(x[7]), reverse=True)[0]
    print(*house_array[0])  # 输出标题行，空格间隔
    print(*result_ls)  # 输出前1名的数据
elif n == '精装电梯房单价':
    # 构建筛选条件
    filter_criteria = ('有电梯' == house_array[1:, 6]) & (house_array[1:, 5] == '精装')
    # 条件删选获得所有精装电梯房的面积和价格，得到新数组
    result_array = house_array[1:][filter_criteria][:, 7:9].astype(float)
    # 计算精装电梯房单价
    print(f'{np.sum(result_array[:,1])/np.sum(result_array[:,0]):.2f}万元')
elif n == '房屋朝向':
    s = input()
    # 获取朝向为输入值s的个数
    result_count = sum(s == house_array[1:, 3])
    # 条件表达式，根据结果列表长度是否为0，输出不同内容
    print(f'{result_count}套') if result_count != 0 else print('无数据')
else:
    # 判断那些行小区名中包含n，返回布尔数组
    filter_array = np.char.count(house_array[1:, 1], n) != 0
    print(*house_array[0])  # 输出标题行，空格间隔
    # 条件表达式，根据结果长度是否为0，输出不同内容。不为0时，利用列表推导式，循环输出结果数组的数据
    print('未找到相关数据') if sum(filter_array) == 0 else [print(*i) for i in house_array[1:][filter_array]]
