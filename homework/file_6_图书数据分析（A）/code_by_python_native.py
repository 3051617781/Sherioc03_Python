with open('step6/CBOOK.csv', 'r', encoding='utf-8') as f:
    ls = [line.strip().split(',') for line in f][1:]  # 推导式实现文件转二维列表，并切片去除标题行
cmd = input()
if cmd == 'record':
    print(len(ls))  # 列表元素个数即为图书数据的总数量
elif cmd == 'rank':
    no = input()
    book_dict = {i[0]: i for i in ls}  # 字典推导式，书籍编号为键，书籍信息列表为值
    print(*book_dict[no], sep='\n')  # 根据输入编号获取信息列表后，解包输出，换行间隔
elif cmd == 'maxcomment':
    # 对列表按评论数（需切片去除后面的‘条评论’并转为浮点数）降序排列，切片获取排序后的前十名
    # 列表推导式，前10名每条数据的书名和评论数拼接成字符串作为列表元素
    # 解包输出推导出的列表，换行间隔
    print(*[i[1]+' '+i[5] for i in sorted(ls, key=lambda x:float(x[5][:-3]), reverse=True)[:10]], sep='\n')
elif cmd == 'maxname':
    n = int(input())
    # 对列表按书名长度降序排列，切片获取排序后的前n名
    # 列表推导式，前n名每条数据的书名作为列表元素
    # 解包输出推导出的列表，换行间隔
    print(*[i[1] for i in sorted(ls,  key=lambda x:len(x[1]), reverse=True)[:n]], sep='\n')
else:
    print('无数据')
