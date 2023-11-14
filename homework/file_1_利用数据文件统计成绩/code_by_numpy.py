import numpy as np

score_array = np.loadtxt('step1/成绩单.csv', delimiter=',', dtype=str, encoding='utf-8')
n = int(input())
score_sorted_array = np.array(sorted(score_array, key=lambda x: int(x[9])))
print('最低分{}分,最高分{}分'.format(score_sorted_array[0, 9], score_sorted_array[-1, 9]))
print(score_sorted_array[:n].tolist())  # 输出前n名同学成绩信息
print(score_sorted_array[-n:].tolist())  # 输出后n名同学成绩信息
print([round(np.mean(score_sorted_array[:, i].astype(float)), 2) for i in range(3, 9)])  # 列表推导式求每道题的平均分
