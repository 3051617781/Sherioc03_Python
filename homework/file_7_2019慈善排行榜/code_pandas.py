import pandas as pd

data = pd.read_csv('step7/2019Charity.csv', encoding='utf-8')
n = input()
if n.lower() == 'total':
    # 求慈善捐款列的总额
    print('Total:{}万元'.format(data['现金捐赠总额（万元）'].sum()))
elif n.isdigit() and 1 <= eval(n) <= 100:  # 输入为1-100之间的排名编号
    [print(*i) for i in data[data['排名'] == eval(n)].values]  # 筛选出排名列为n的行，循环解包输出数据
elif n in data['总部（省份）'].drop_duplicates().values:  # 省份列去重，用于判断输入省份是否合法
    result = data[data['总部（省份）'] == n]  # 过滤出所有省份为n的记录
    [print(*i) for i in result.loc[:, '排名':'总部（省份）'].values]  # 利用列表推导式，循环解包输出结果每行前4列数据
else:
    print('No Record')
