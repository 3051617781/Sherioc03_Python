import numpy as np

iris_sepal_length = np.loadtxt("step3/iris_sepal_length.csv", delimiter=",")  # 读取文件到数组
iris_sepal_length = np.unique(iris_sepal_length)  # 去掉重复的花萼数据
iris_sepal_length = np.sort(iris_sepal_length)  # 按花萼数据从小到大排序
n = int(input())
iris_sepal_length = iris_sepal_length[:n]  # 切片前n个
print(f'花萼长度的最大值是：{np.max(iris_sepal_length):.2f}')  # 最大值
print(f'花萼长度的最小值是：{np.min(iris_sepal_length):.2f}')  # 最小值
print(f'花萼长度的均值是：{np.mean(iris_sepal_length):.2f}')  # 均值
print(f'花萼长度的方差是：{np.var(iris_sepal_length):.2f}')  # 标准差
print(f'花萼长度的标准差是：{np.std(iris_sepal_length, ddof=1):.2f}')  # 方差
