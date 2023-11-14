import numpy as np


# 返回指定数组（data_array）中指定列（colum）值与给定值（value）满足type指定条件（1大于等于；0小于等于)的所有数据
def select_data(data_array, column, value, is_ge=1):
    if is_ge:
        return data_array[data_array[:, column].astype(float) >= value]
    else:
        return data_array[data_array[:, column].astype(float) <= value]


# 返回指定数组（data_array）中指定列（colum）的平均值、最大值和最小值
def get_statistics(data_array, column):
    statistics_data = data_array[:, column].astype(float)
    return statistics_data.mean(), statistics_data.max(), statistics_data.min()


student_data = np.loadtxt('step5/admit2.csv', str, delimiter=',', skiprows=1, encoding='utf-8')
cmd = input()
if cmd == '1':
    # 获取录取概率大于等于80%的记录
    admit_ge_80 = select_data(student_data, -1, 0.8)
    # 获取录取概率大于等于80%的记录中大学排名评分大于等于4分的记录
    rating_ge_4 = select_data(admit_ge_80, 1, 4)
    print(f'Top University in >=80%:{len(rating_ge_4)/len(admit_ge_80)*100:.2f}%')
elif cmd == '2':
    # 获取录取概率大于等于80%的记录
    admit_ge_80 = select_data(student_data, -1, 0.8)
    toefl_result = get_statistics(admit_ge_80, 3)
    print('TOEFL Average Score:{:.2f}\nTOEFL Max Score:{:.2f}\nTOEFL Min Score:{:.2f}'.format(*toefl_result))
elif cmd == '3':
    # 获取录取概率大于等于80%的记录
    admit_ge_80 = select_data(student_data, -1, 0.8)
    cgpa_result = get_statistics(admit_ge_80, 4)
    print('CGPA Average Score:{:.3f}\nCGPA Max Score:{:.3f}\nCGPA Min Score:{:.3f}'.format(*cgpa_result))
elif cmd == 'Research':
    # 获取录取概率大于等于90%的记录
    admit_ge_90 = select_data(student_data, -1, 0.9)
    # 获取录取概率大于等于90%的记录中有研究经历的记录
    research_admit_ge_90 = select_data(admit_ge_90, 5, 0.5)
    # 获取录取概率小于等于70%的记录
    admit_le_70 = select_data(student_data, -1, 0.7, is_ge=0)
    # 获取录取概率小于等于70%的记录中有研究经历的记录
    research_admit_le_70 = select_data(admit_le_70, 5, 0.5)
    print(f'Research in >=90%:{len(research_admit_ge_90) / len(admit_ge_90) * 100:.2f}%')
    print(f'Research in <=70%:{len(research_admit_le_70) / len(admit_le_70) * 100:.2f}%')
else:
    print('ERROR')
