import numpy as np

book_data = np.loadtxt('step6/CBOOK.csv', str, delimiter=',', skiprows=1, encoding='utf-8')
cmd = input()
if cmd == 'record':
    print(book_data.shape[0])  # 数组shape中行数即为图书数据的总数量
elif cmd == 'rank':
    no = input()
    print(*book_data[book_data[:, 0] == no][0], sep='\n')  # 根据输入编号获取相应行信息后，解包输出，换行间隔
elif cmd == 'maxcomment':
    # 对评论数（需去除后面的‘条评论’并转为整数）降序排列(通过取负实现)，切片获取排序后的前十名的行号
    sorted_arg = np.argsort(-np.char.replace(book_data[:, 5], '条评论', '').astype(int))[:10]
    # 切片获取对应行的书名和评论列，利用列表推导式依次解包输出
    [print(*i) for i in book_data[sorted_arg, 1:6:4]]
elif cmd == 'maxname':
    n = int(input())
    # 对书名长度降序排列(通过取负实现)，切片获取排序后的前n名的行号
    sorted_arg = np.argsort(-np.char.str_len(book_data[:, 1]))[:n]
    # 切片获取对应行的书名，利用列表推导式依次输出
    [print(i) for i in book_data[sorted_arg, 1]]
else:
    print('无数据')
