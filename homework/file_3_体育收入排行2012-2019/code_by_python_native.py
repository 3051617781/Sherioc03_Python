with open('step3/2012-19sport.csv', 'r', encoding='utf-8') as f:
    ls = [line.strip().split(',') for line in f][1:]  # 推导式实现文件转二维列表，并切片去除标题行
cmd = input()
if cmd.isdigit() and 2012 <= int(cmd) <= 2019:  # 如果输入cmd是2012-2019之间的整数
    k = int(input())
    for j in [i for i in ls if i[6] == cmd][:k]:  # 列表推导式获取cmd年数据列表，再切片获取前k名后，遍历输出
        print(' | '.join(j).strip('#'))  # 每个元素先拼接为字符串，再去除开头的#号后输出
elif cmd.lower() == 'sport':  # 如果输入lower()归一化为小写后为sport
    year = input()
    sport_ls = sorted({i[5] for i in ls if i[6] == year})  # 集合推导式获取该年运动项目的集合（自动去重）后，获取其排序后的列表
    sport_dict = dict(zip(range(1, len(sport_ls)+1), sport_ls))  # 序号为键，运动项目为值，构建字典
    # 通过遍历字典键值对，输出选择菜单
    for i in sport_dict.items():
        print(*i, sep=': ')
    n = int(input())
    # 列表推导式获取year年指定运动项目（运动项目通过字典获取）的数据列表
    result_ls = [i for i in ls if i[6] == year and i[5] == sport_dict[n]]
    # 列表推导式获取year年指定运动项目的所有收入数据构成的列表，收入字符串需通过切片去除前面的‘$’和后面的‘ M’，再转为浮点数
    incoming_ls = [float(i[2][1:-2]) for i in result_ls]
    for i in result_ls:
        print(' | '.join(i).strip('#'))  # 每个元素先拼接为字符串，再去除开头的#号后输出
    print(f'TOTAL: ${sum(incoming_ls):.2f} M')  # 收入列表求和即为总收入
else:
    print('Wrong Input')
