import numpy as np

cmd = input().lower()
if cmd == 'array':
    ls = eval(input())  # 输入转换为列表
    print(np.array(ls))
elif cmd == 'arange':
    param = map(int, input().split())  # 输入拆分
    print(np.arange(*param))  # 解包作为参数
elif cmd == 'linspace':
    param = map(int, input().split())
    print(np.linspace(*param))
elif cmd == 'logspace':
    param = list(map(int, input().split()))
    print(np.logspace(*param[:3], endpoint=False, base=param[-1]))
elif cmd == 'zeros':
    param = tuple(map(int, input().split()))  # 输入拆分为元组
    print(np.zeros(param))
elif cmd == 'ones':
    param = tuple(map(int, input().split()))  # 输入拆分为元组
    print(np.ones(param))
elif cmd == 'full':
    param = tuple(map(int, input().split()))  # 输入拆分为元组
    print(np.full(param[:2], param[-1]))
elif cmd == 'identity':
    param = int(input())
    print(np.identity(param))
elif cmd == 'randint':
    param = tuple(map(int, input().split()))  # 输入拆分为元组
    np.random.seed(param[0])
    print(np.random.randint(param[1], high=param[2], size=param[-2:]))
else:
    print('ERROR')
