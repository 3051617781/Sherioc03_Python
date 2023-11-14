import numpy as np


def gen_stu_id(in_year, school, major, c_name, rank, school_dict, major_dict):
    """
    定义普通函数，根据学生信息、班内排名和学院代码、专业代码字典，拼接学号。
    拼接规则：012+入学年份后两位+学院代码+专业代码+班级名称后四位+班内排名（不足两位时左补0到两位）
    :param in_year: 入学年份
    :param school: 学院名称
    :param major: 专业名称
    :param c_name: 班级名称
    :param rank: 班级排名
    :param school_dict: 学院编号字典
    :param major_dict: 专业编号字典
    :returns: 拼接出的学号
    """
    return '012' + in_year[-2:] + school_dict[school] + major_dict[major] + c_name[-4:] + f'{rank:02d}'


def get_class_member(stu_array, c_name):
    """
    根据班级名（cname）获取所有班级成员信息
    :param stu_array: 学生信息数组
    :param c_name: 班级名称
    :returns: 该班所有学生的信息数组
    """
    return stu_array[stu_array[:, -2] == c_name]


def gen_stu_id_by_class(class_array, school_dict, major_dict, s_name=None):
    """
    为班级所有人生成学号，根据s_name返回添加学号后的学生信息数组
    :param class_array: 班级学生信息数组
    :param school_dict: 学院编号字典
    :param major_dict: 专业编号字典
    :param s_name: 学生名。为None，返回班级所有成员信息数组；否则，返回名字为s_name的成员信息
    :returns: 根据s_name返回添加学号后的学生信息数组
    """
    # 将普通函数gen_stu_id转化为转换为能对数组的每个元素进行计算的ufunc函数，7为输入参数个数，1为返回值个数
    gen_stu_id_ufunc = np.frompyfunc(gen_stu_id, 7, 1)
    # 调用函数，求每个成员学号构成的数组
    stu_id_array = gen_stu_id_ufunc(class_array[:, -1], class_array[:, 2], class_array[:, 3], class_array[:, 4],
                                    np.arange(1, len(class_array) + 1), school_dict, major_dict)
    # 学号数组插入到最前面，作为第一列
    class_array = np.insert(class_array, 0, stu_id_array, axis=1)
    if s_name:
        return class_array[class_array[:, 1] == s_name]
    else:
        return class_array


def output(output_data):
    """
    输出函数，按格式要求输出
    :param output_data: 待输出数组
    :returns: 无返回值
    """
    [print(*item) for item in output_data]  # 利用列表推导式，将数组每行解包输出


# 获取学院代码字典，key为学院名，value为学院代码
school_code_dict = dict(np.loadtxt('step5/schoolCode.csv', str, delimiter=',', encoding='utf-8'))
# 获取专业代码字典，key为专业名，value为学院代码
major_code_dict = dict(np.loadtxt('step5/MajorCode.csv', str, delimiter=',', encoding='utf-8'))
# 读取学生信息数据到数组，此处类型蛇者为object，避免后面插入的学号超过Numpy中字符串默认长度而无法显示
student_array = np.loadtxt('step5/studentList.csv', object, delimiter=',', encoding='utf-8')
stu_name = input()
class_name = input()
# 根据输入的学生名，输出该学生含学号的所有信息
class_member_by_stu_name = get_class_member(student_array, student_array[student_array[:, 0] == stu_name][0][-2])
output(gen_stu_id_by_class(class_member_by_stu_name, school_code_dict, major_code_dict, s_name=stu_name))
# 根据输入的班级名，输出该班所有学生含学号的所有信息
class_member_by_class_name = get_class_member(student_array, class_name)
output(gen_stu_id_by_class(class_member_by_class_name, school_code_dict, major_code_dict))
