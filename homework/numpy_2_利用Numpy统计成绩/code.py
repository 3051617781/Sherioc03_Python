import numpy as np

# numpy读取文件到数组，元素数据类型为字符串
scoreAll = np.loadtxt('step2/成绩单数字.csv', dtype=str, delimiter=',', encoding='utf-8')
# 数组scoreAll中非数值型字符串去掉,转为整型，生成成绩数组
scoreNum = scoreAll[1:, 2:].astype(int)
name = input()
course = input()
# 获取该姓名在数组中的行列号，返回形如[[1][1]]的二维数组，前面是行号，后面是列号
indexName = np.where(scoreAll == name)
# 从成绩数组中切片出该学生所有成绩所在行
stu_score = scoreNum[indexName[0][0]-1]
print(f'{name}同学的总分为{np.sum(stu_score):.2f}')
print(f'{name}同学的平均分为{np.average(stu_score):.2f}')
# 获取该课程名在数组中的行列号
indexCourse = np.where(scoreAll == course)
# 从成绩数组中切片出该课程所有成绩所在列
course_score = scoreNum[:, indexCourse[1][0]-2]
print(f'{course}课程平均成绩为{np.average(course_score):.2f}')
print(f'{course}课程中位数为{np.median(course_score):.2f}')
print(f'{course}课程标准差为{np.std(course_score):.2f}')
