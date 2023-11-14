ls = []
while temp := input():  # 海象运算符，自行查阅官方文档
    ls.append(temp.split())
print(sorted(ls, key=lambda x: float(x[1][:-1]) * 1000 if x[1][-1] == 't' else float(x[1][:-2])))
