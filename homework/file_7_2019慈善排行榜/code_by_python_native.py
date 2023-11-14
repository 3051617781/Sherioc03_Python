with open('step7/2019Charity.csv', 'r', encoding='UTF-8') as f:
    ls = [line.strip().split(',') for line in f][1:]  # 推导式实现文件转二维列表，并切片去除标题行
n = input()
if n.lower() == 'total':
    # 列表推导式，获取所有慈善捐款构成的列表，列表求和即为慈善捐款的总额
    print('Total:{}万元'.format(sum([eval(i[-1]) for i in ls])))
elif n.isdigit() and 1 <= eval(n) <= 100:  # 输入为1-100之间的排名编号
    result_ls = [i for i in ls if i[0] == n]  # 列表推导式，过滤出所有排名编号为n的记录
    [print(*i) for i in result_ls]  # 利用列表推导式，循环解包输出列表数据
elif n in {i[3] for i in ls}:  # 集合推导式获取所有省份集合，用于判断输入省份是否合法
    result_ls = [i[:4] for i in ls if i[3] == n]  # 列表推导式，过滤出所有省份为n的记录，并取其前4个元素的切片构成新列表
    [print(*i) for i in result_ls]  # 利用列表推导式，循环解包输出列表数据
else:
    print('No Record')
