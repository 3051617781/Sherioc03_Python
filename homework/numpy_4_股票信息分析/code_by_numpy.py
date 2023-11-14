import numpy as np


def get_top_n(n, data_array, order_by, reverse=1):
    """
    根据order_by指定的列排序data_array并返回前n项。
    :param n: 需返回的项数
    :param data_array: 待排序的数组
    :param order_by: 排序依据列索引
    :param reverse: 升序（1）或降序（-1），默认升序
    :returns: 排序后的数组前n行
    """
    return data_array[(np.argsort(reverse*data_array[:, order_by].astype(float), kind='stable'))[:n]]


def output(output_data, title='', unit=''):
    """
    根据order_by指定的列排序data_array并返回前n项。
    :param output_data: 待输出数组
    :param title: 标题行字符串，默认为空
    :param unit: 单位字符串，默认为空
    :returns: 无返回
    """
    if title:   # 标题不为空则输出标题
        print(title)
    [print(*item, end=unit+'\n') for item in output_data]  # 利用列表推导式，将数组每行解包输出，并在末尾加上单位和换行


def search_by_date(date_str, data_array):
    """
    按日期搜索该数组中该日期的数据。
    :param date_str: 日期字符串
    :param data_array: 数据数组
    :returns: 该日期的所有数据构成的数组
    """
    return data_array[data_array[:, 0] == date_str]


stock_data = np.loadtxt('step4/China Minsheng Bank.csv', str, delimiter=',', skiprows=1, encoding='utf-8')
cmd = input()
if cmd == '最高价':
    num = int(input())
    top_high = get_top_n(num, stock_data, 4, reverse=-1)
    output(top_high[:, [0, 4]], title=f'最高价从高到低前{num}名:', unit='元')
elif cmd == '开盘价':
    num = int(input())
    bottom_open = get_top_n(num, stock_data, 6)
    output(bottom_open[:, [0, 6]], title=f'开盘价从低到高前{num}名:', unit='元')
elif cmd == '成交金额':
    num = int(input())
    top_amount = get_top_n(num, stock_data, -1, reverse=-1)
    print(f'成交金额最多的{num}天成交额为{top_amount[:,-1].astype(np.int64).sum()}元')
elif cmd == '日期':
    day_str = input()
    date_data = search_by_date(day_str, stock_data)
    output(date_data)
