with open('step1/成绩单.csv', 'r', encoding='utf-8') as data:
    score = [line.strip().split(',') for line in data]  # 推导式实现文件转二维列表
n = int(input())
score.sort(key=lambda x: int(x[9]))  # 按总分升序排序
print('最低分{}分,最高分{}分'.format(score[0][9], score[-1][9]))
print(score[:n])  # 输出前n名同学成绩信息
print(score[-n:])  # 输出后n名同学成绩信息
print([round(sum(int(x[i]) for x in score) / len(score), 2) for i in range(3, len(score[0])-1)])  # 列表推导式求每道题的平均分
