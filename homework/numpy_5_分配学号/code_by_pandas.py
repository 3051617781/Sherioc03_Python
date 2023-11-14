import pandas as pd


# 根据班级名（cname）获取所有班级成员信息
def get_class_member(stu_data, cname):
    return stu_data[stu_data['class'] == cname]


# 为班级所有人生成学号，根据sname返回（None，返回所有成员；否则，返回名字为sname的成员）
def gen_stuid_by_class(class_data, school_dict, major_dict, sname=None):
    class_data.index = (range(len(class_data)))
    # 获取班级所有学生的学院码
    school_ids = pd.DataFrame([school_dict[i] for i in class_data['school']], dtype=str)
    # 获取班级所有学生的专业码
    major_ids = pd.DataFrame([major_dict[i] for i in class_data['major']], dtype=str)
    # 构造学生班内序号
    stu_orders = pd.DataFrame([f'{i:02d}' for i in range(1, len(class_data)+1)], dtype=str)
    # 拼接所有学生的学号
    stu_ids = '012' + class_data['year'].str[-2:] + school_ids[0]+major_ids[0]+class_data['class'].str[-4:]+stu_orders[0]
    # 学号插入到最前面，作为第一列
    class_data.insert(0, 'stu_id', stu_ids)
    if sname:
        return class_data[class_data['name'] == sname]
    else:
        return class_data


# 输出函数，按格式要求输出
def output(output_data):
    for item in output_data.values:
        print(*item)


# 获取学院代码字典，key为学院名，值为学院代码
school_code_dict = pd.read_csv('step5/schoolCode.csv', dtype=str, header=None, index_col=0, encoding='utf-8')[1].to_dict()
# 获取学院代码S字典，key为学院名，值为专业代码
major_code_dict = pd.read_csv('step5/MajorCode.csv', dtype=str, header=None, index_col=0, encoding='utf-8',)[1].to_dict()
# 读取学生信息数据
student_data = pd.read_csv('step5/studentList.csv', dtype=str, header=None, names=['name', 'sex', 'school', 'major', 'class', 'year'], encoding='utf-8')
stu_name = input()
class_name = input()
# 根据输入的学生名，输出该学生含学号的所有信息
# 根据输入的学生名，获取学生所在班级，再进一步获取该班级所有成员
class_member_by_sname = get_class_member(student_data, student_data[student_data['name'] == stu_name].iloc[0]['class'])
output(gen_stuid_by_class(class_member_by_sname, school_code_dict, major_code_dict, sname=stu_name))
# 根据输入的班级名，输出该班所有学生含学号的所有信息
class_member_by_cname = get_class_member(student_data, class_name)
output(gen_stuid_by_class(class_member_by_cname, school_code_dict, major_code_dict))
