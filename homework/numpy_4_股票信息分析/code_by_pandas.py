import pandas as pd


# 根据order_by指定的列排序data并返回前n项。ascending=True升序；ascending=False降序
def get_top_n(n, data, order_by, ascending=False):
    return data.sort_values(by=order_by, kind='stable', ascending=ascending)[:n]


# 输出函数，按格式要求输出
def output(output_data, title='', unit=''):
    if title:
        print(title)
    for item in output_data.values:
        print(*item, end=unit+'\n')


# 按日期搜索，返回日期相同的所有数据
def search_by_date(date_str, data):
    return data[data['日期'] == date_str]


stock_data = pd.read_csv('step4/China Minsheng Bank.csv',  encoding='utf-8')
cmd = input()
if cmd == '最高价':
    num = int(input())
    top_high = get_top_n(num, stock_data, '最高价')
    output(top_high[['日期', '最高价']], title=f'最高价从高到低前{num}名:', unit='元')
elif cmd == '开盘价':
    num = int(input())
    bottom_open = get_top_n(num, stock_data, '开盘价', ascending=True)
    output(bottom_open[['日期', '开盘价']], title=f'开盘价从低到高前{num}名:', unit='元')
elif cmd == '成交金额':
    num = int(input())
    top_amount = get_top_n(num, stock_data, '成交金额')
    print(f'成交金额最多的{num}天成交额为{top_amount["成交金额"].sum()}元')
elif cmd == '日期':
    day_str = input()
    date_data = search_by_date(day_str, stock_data)
    output(date_data)
