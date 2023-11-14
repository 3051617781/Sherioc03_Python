with open('step4/university.csv', 'r', encoding='utf-8') as f:
    school_title_str = f.readline().strip()  # 首行去末尾回车，得到标题字符串
    # 后续行通过字典推导式得到数据字典，该行学校名为键，该行去末尾回车的字符串为值
    school_dict = {line.strip().split(',')[1]: line.strip() for line in f}
school_name = input()
print(school_title_str)  # 输出标题行
print(school_dict.get(school_name))  # 通过学校名查询字典，获取学校信息后输出