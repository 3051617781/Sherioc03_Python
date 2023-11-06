"""
03 根据序号输出对应诗
"""
#query_poem中if elif 语句设计
def read_file(file: str) -> list:
    """利用列表推导式读txt文件中的数据到一维列表，并返回列表"""
    with open(file, 'r',encoding='utf-8') as fr:  # 以读模式创建文件对象
        data_list = [line.strip() for line in fr]
    return data_list               # 返回列表


def query_poem(poem_list: list, poem_title: str) -> None:
    """遍历列表，根据诗题输出对应唐诗内容"""
    flag = 0  # 控制输入输出的标记，为0时不输出，为1时输出
    for item in poem_list:
        # 若某行前三位与输入序号相同，且诗题在切分出的列表中，则输出标题。同时将flag设置为1，保证输出后续诗句
        if item[:3].isdigit() and poem_title in item.split("："):  
            print(item[3:])
            flag = 1
        elif flag == 1:
            if item[:3].isdigit():  # 若flag为1时，又出现某行前三位为数字，则为下首诗的标题。意味着已输出完毕，结束循环
                break
            else:
                print(item)  # 否则输出诗句

if __name__ == '__main__':
    path = './src/'
    filename = '唐诗三百首.txt'
    data = read_file(path+filename)
    num = input("请输入010-320的三位序号：")
    # title = input("请输入诗题：")
    query_poem(data, num)