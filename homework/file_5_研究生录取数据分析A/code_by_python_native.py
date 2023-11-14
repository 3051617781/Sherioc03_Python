with open('step5/admit2.csv', 'r', encoding='utf-8') as f:
    ls = [line.strip().split(',') for line in f][1:]  # 推导式实现文件转二维列表，并切片去除标题行
n = input()
if n == '1':
    coa_80_ls = [i for i in ls if float(i[-1]) >= 0.8]  # 列表推导式过滤出录取概率大于等于80%的记录构成的列表
    ur_40_ls = [i for i in coa_80_ls if float(i[1]) >= 4]  # 列表推导式从coa_80_ls中过滤出大学排名评分大于等于4分的记录构成的列表
    print(f'Top University in >=80%:{len(ur_40_ls)/len(coa_80_ls)*100:.2f}%')  # 计算百分比
elif n == '2':
    # 列表推导式过滤出录取概率大于等于80%的记录构成的列表，并按TOEFL分数升序排序
    coa_80_ls = sorted([i for i in ls if float(i[-1]) >= 0.8], key=lambda x: float(x[3]))
    # 列表推导式获取TOEFL分数列表，列表求和，再除以列表长度，计算平均分
    print(f'TOEFL Average Score:{sum([float(i[3]) for i in coa_80_ls])/len(coa_80_ls):.2f}')
    print(f'TOEFL Max Score:{float(coa_80_ls[-1][3]):.2f}')  # 输出最高分
    print(f'TOEFL Min Score:{float(coa_80_ls[0][3]):.2f}')  # 输出最低分
elif n == '3':
    # 列表推导式过滤出录取概率大于等于80%的记录构成的列表，并按绩点升序排序
    coa_80_ls = sorted([i for i in ls if float(i[-1]) >= 0.8], key=lambda x: float(x[4]))
    # 列表推导式获取绩点列表，列表求和，再除以列表长度，计算平均绩点
    print(f'CGPA Average Score:{sum([float(i[4]) for i in coa_80_ls])/len(coa_80_ls):.3f}')
    print(f'CGPA Max Score:{float(coa_80_ls[-1][4]):.3f}')  # 输出最高分
    print(f'CGPA Min Score:{float(coa_80_ls[0][4]):.3f}')  # 输出最低分
elif n == 'Research':
    coa_90_ls = [i for i in ls if float(i[-1]) >= 0.9]  # 列表推导式过滤出录取概率大于等于90%的记录构成的列表
    coa_70_ls = [i for i in ls if float(i[-1]) <= 0.7]  # 列表推导式过滤出录取概率小于等于70%的记录构成的列表
    coa_90_re_ls = [i for i in coa_90_ls if i[5] == '1']  # 列表推导式从coa_90_ls中过滤出有研究经历的记录构成的列表
    coa_70_re_ls = [i for i in coa_70_ls if i[5] == '1']  # 列表推导式从coa_70_ls中过滤出有研究经历的记录构成的列表
    print(f'Research in >=90%:{len(coa_90_re_ls)/len(coa_90_ls)*100:.2f}%')
    print(f'Research in <=70%:{len(coa_70_re_ls)/len(coa_70_ls)*100:.2f}%')
else:
    print('ERROR')
