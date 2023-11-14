import numpy as np

# 读取时利用converters去除最后一列某些行多余的空格
data = np.loadtxt('step7/2019Charity.csv', str, delimiter=',', skiprows=1,
                  converters={5: lambda x: x.strip()}, encoding='utf-8')
n = input()
if n.lower() == 'total':
    # 求慈善捐款列的总额
    print('Total:{}万元'.format(data[:, -1].astype(int).sum()))
elif n.isdigit() and 1 <= eval(n) <= 100:  # 输入为1-100之间的排名编号
    [print(*i) for i in data[data[:, 0] == n]]  # 筛选出第一列为n的行，循环解包输出数据
elif n in np.unique(data[:, 3]):  # 数组省份列去重，用于判断输入省份是否合法
    result = data[data[:, 3] == n]  # 过滤出所有省份为n的记录
    [print(*i) for i in result[:, :4]]  # 利用列表推导式，循环解包输出结果每行前4列数据
else:
    print('No Record')
