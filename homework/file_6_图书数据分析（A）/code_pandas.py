import pandas as pd

# 数据以字符串读入，避免输出格式错误.以编号为行标签
book_data = pd.read_csv('step6/CBOOK.csv', encoding='utf-8', dtype=str, index_col='编号')
# 添加两列，用于排序
book_data['count'] = book_data['评论数'].str.slice(0, -3, 1).astype(int)
book_data['length'] = book_data['书名'].str.len()
cmd = input()
if cmd == 'record':
    print(len(book_data))  # 行数即为图书数据的总数量
elif cmd == 'rank':
    no = int(input())
    print(no)
    print(*book_data.loc[no, '书名':'推荐指数'], sep='\n')  # 根据输入编号获取相应行信息)(排除后加的列)后，解包输出，换行间隔
elif cmd == 'maxcomment':
    # 对DataFrame按count降序排序后，截取前10名
    result = book_data.sort_values(by='count', axis=0, kind='stable', ascending=False)[:10]
    # 切片获取对应行的书名和评论列，利用列表推导式依次解包输出
    [print(*i) for i in result[['书名', '评论数']].values]
elif cmd == 'maxname':
    n = int(input())
    # 对DataFrame按length降序排序后，截取前n名
    result = book_data.sort_values(by='length', axis=0, kind='stable', ascending=False)[:n]
    # 切片获取对应行的书名列，利用列表推导式依次解包输出
    [print(i) for i in result['书名'].values]
else:
    print('无数据')
