import math        # 导入math库

a = eval(input())
b = eval(input())
c = eval(input())
s = (a + b + c) / 2.0
m = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# m=math.sqrt(s * (s - a) * (s - b) * (s - c))    # 第二种开根号方法
print("周长={:.2f}".format(a + b + c))
print("面积={:.2f}".format(m))