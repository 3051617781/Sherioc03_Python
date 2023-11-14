import pandas as pd

fdata = pd.read_csv('pandas_10/tips.csv')
op = input()
if op == 'gender':
    temp = fdata.groupby('gender')['tip'].mean()
    print(f'男性顾客平均小费为：{temp.loc["Male"]:.2f}')
    print(f'女性顾客平均小费为：{temp.loc["Female"]:.2f}')
elif op == 'day':
    temp = fdata.groupby('day')['tip'].mean().sort_values()
    [print(f'{i}：{temp.loc[i]:.2f}') for i in temp.index]
elif op == 'time':
    temp1 = fdata.groupby('time')['tip'].mean()
    temp2 = fdata.groupby('time')['total_bill'].agg(['count', 'sum', 'mean'])
    print(f"午餐时间共{temp2.loc['Lunch','count']}条记录，"
          f"共消费{temp2.loc['Lunch','sum']:.2f}，"
          f"平均每单消费{temp2.loc['Lunch','mean']:.2f}，"
          f"平均小费{temp1.loc['Lunch']:.2f}")
    print(f"晚餐时间共{temp2.loc['Dinner','count']}条记录，"
          f"共消费{temp2.loc['Dinner','sum']:.2f}，"
          f"平均每单消费{temp2.loc['Dinner','mean']:.2f}，"
          f"平均小费{temp1.loc['Dinner']:.2f}")
elif op == 'smoker':
    gender = input()
    temp = fdata[(fdata['smoker'] == 'Yes') & (fdata['gender'] == gender) & (fdata['total_bill'] > 30)].copy()
    temp['total_bill'] = temp['total_bill'].apply(lambda x: f'{x:.2f}')
    temp['tip'] = temp['tip'].apply(lambda x: f'{x:.2f}')
    print(*temp.values.tolist(), sep='\n')
elif op == "average":
    n = int(input())
    fdata['average'] = (fdata['total_bill'] / fdata['size'])
    temp = fdata.sort_values(by=['average'], ascending=False).head(n).iloc[:, :7].copy()
    temp['total_bill'] = temp['total_bill'].apply(lambda x: f'{x:.2f}')
    temp['tip'] = temp['tip'].apply(lambda x: f'{x:.2f}')
    print(*temp.values.tolist(), sep='\n')
else:
    print("无数据")
