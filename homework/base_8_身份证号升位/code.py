id_fifteen = input()  # 输入15位身份证号
wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 第i 位置上的加权因子
ecc = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # 校验码
sum_ai_wi = 0  # 身份证前十七位数分别乘以不同系数并求和，初值为0
j = 0  # 指向第一位
if int(id_fifteen[6:8]) >= 5:  # 第六位数后面插入19 （1905 年1 月1 日以后出生）
    id_seventeen = id_fifteen[0:6] + '19' + id_fifteen[6:]
else:  # 第六位数后面插入20（2000.1.1-2004.12.31 出生）
    id_seventeen = id_fifteen[0:6] + '20' + id_fifteen[6:]
for i in id_seventeen:  # 遍历17位的身份证号
    sum_ai_wi = sum_ai_wi + int(i) * wi[j]  # 身份证前十七位数分别乘以不同系数并求和
    j = j + 1  # 指向下一位
id_eighteen = id_seventeen + ecc[sum_ai_wi % 11]  # 根据余数查ecc列表对应序号取得最后一位的字符，拼接到一起
print(id_eighteen)  # 输出18位身份证号
