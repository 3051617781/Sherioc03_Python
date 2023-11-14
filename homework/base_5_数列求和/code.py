A = input()
num = int(input())
if 1 <= int(A) <= 9 and num >= 0:
	print(sum([int(A * i) for i in range(1, num + 1)]))
else:
	print('data error')
