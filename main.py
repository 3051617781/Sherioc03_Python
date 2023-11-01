def read_file(file: str):
    with open(file, 'r',encoding='utf-8')as fr:
        #去除标点符号
        data_dict = [line.strip(',').strip('').split() for line in fr]
    return data_dict

path = 'article.txt'
data_dict = read_file(path)
#将每个单词转换为小写
word_list = [i.lower() for item in data_dict for i in item]
#使用set去重、sorted按字典序排序
words = sorted(list(set(word_list)))
#统计word_list中每个单词的数量
word_dict = dict.fromkeys(words, 0)
for word in word_list:
    for key in word_dict.keys():
        if key == word:
            word_dict[key] += 1
print(word_dict)
