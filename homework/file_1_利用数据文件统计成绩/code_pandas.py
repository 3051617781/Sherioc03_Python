import pandas as pd

# 读取时设置学号列类型为str，避免前面的0丢失
score_df = pd.read_csv('step1/成绩单.csv', delimiter=',', dtype={2: str}, header=None, encoding='utf-8')
n = int(input())
score_sorted_df = score_df.sort_values(by=9, axis=0, kind='mergesort')  # 采用合并排序，保证稳定
print('最低分{}分,最高分{}分'.format(score_sorted_df.iloc[0][9], score_sorted_df.iloc[-1][9]))
print(score_sorted_df[:n].values.astype(str).tolist())  # 输出前n名同学成绩信息
print(score_sorted_df[-n:].values.astype(str).tolist())  # 输出后n名同学成绩信息
print(score_sorted_df[range(3, 9)].mean(axis=0).round(2).values.tolist())  # 求每道题的平均分
