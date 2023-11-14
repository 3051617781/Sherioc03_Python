def method_of_set(n):
    name = input()  # 吉林,湖北,湖南
    my_set = set(name.split())  # 输入转集合
    for i in range(n):
        ls = input().split()  # 输入命令及参数，之间用空格分隔
        if ls[0] == 'print':  # 如要输入的命令是“print”，集合转列表输出
            print(sorted(list(my_set)))
        elif ls[0] == 'update':  # 如要输入的命令是“update”，用name中的元素修改集合
            my_set.update(set(ls[1:]))
        elif ls[0] == 'add':  # 如要输入的命令是“add”，在集合中加入元素name
            my_set.add(ls[1])
        elif ls[0] == 'del':  # 如要输入的命令是“del”，删除集合中的元素name，当name 不存在时，不能引发错误
            my_set.discard(ls[1])
        elif ls[0] == 'clear':  # 如要输入的命令是“clear”，清空集合中全部元素
            my_set.clear()


if __name__ == '__main__':
    num = int(input())  # 输入一个正整数 num
    method_of_set(num)
