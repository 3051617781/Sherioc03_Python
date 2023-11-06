"""
02学生成绩解析
"""
"""
知识点：
1.
    *和**在定义函数时是打包的意思，在调用函数时是解包的意思
    zip(*iterable)将iterator1，iterator2..对应元素打包成元组，返回由元组组成的对象
内部各个元素为(a1,a2),(b1,b2)...
"""
def read_file(filename):
    """接收文件名为参数，读取文件中的数据为二维列表，返回二维列表"""
    with open(filename, 'r', encoding='utf-8') as fr:
        score_ls = [x.strip().split(',') for x in fr]
    return score_ls


def add_total(score_ls):
    """接收二维列表，增加总分，返回新的二维列表"""
    title = score_ls[0]+['总分']
    score_total = [title]
    for line in score_ls[1:]:
        print(str(sum(map(int,line[1:]))))
        score_total.append(line+[str(sum(map(int,line[1:])))])
    return score_total

def get_python(score_ls)->dict:
    return {x[0]:x[3] for x in score_ls[1:]}

def reverse_lst(score_ls)->list:
    return list(zip(*score_ls))
# *score_ls解包列表
#['姓名', 'C语言', 'Java', 'Python', 'C#', 'C++'] 
# ['罗明', '95', '96', '85', '63', '91'] 
# ['朱佳', '75', '93', '66', '85', '88'] 
# ['李思', '86', '76', '96', '93', '67'] 
# ['郑君', '88', '98', '76', '90', '89'] 
# ['王雪', '99', '96', '91', '88', '86']
#再由zip打包对应元素，再用list转为列表，实现矩阵转置
if __name__ == '__main__':
    score_lst = read_file('./src/5.7 score.csv')
    print(add_total(score_lst))
    print(get_python(score_lst))
    print(reverse_lst(score_lst))
