def main(n):
    ls = []
    for i in range(n):
        lsinput = input().split()
        operate = lsinput[0]
        if operate == 'insert':
            ls.insert(int(lsinput[1]), int(lsinput[2]))
        elif operate == 'remove':
            ls.remove(int(lsinput[1]))
        elif operate == 'append':
            ls.append(int(lsinput[1]))
        elif operate == 'sort':
            ls.sort()
        elif operate == 'pop':
            ls.pop()  # 无参数时，弹出最后一个元素
        elif operate == 'reverse':
            ls.reverse()
        elif operate == 'print':
            print(ls)


if __name__ == '__main__':
    N = int(input())
    main(N)
