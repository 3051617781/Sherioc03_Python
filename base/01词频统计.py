"""
01统计小说《谁动了我的奶酪？》中的英文单词的词频，输出出现频率最高的30个单词。

"""
#疑问：
# word_frequency()中，如何统计字典中出现频率前30的单词？

import string
def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，
    过滤掉中文(中文字符及全角符号Unicode编码都大于256),返回字符串 """
    with open(file, 'r', encoding='utf-8') as novel:
        txt = novel.read()  # 读取文件全部内容为字符串
    english_txt = ''.join([x for x in txt if ord(x) < 256])  # 过滤掉中文，拼接为字符串
    return english_txt  # 返回英文文本


def words_lst(text):
    """接收字符串为参数，用空格替换字符串中所有标点符号，根据空格将字符串切分为列表
    返回值为元素为单词的列表。"""
    translator = str.maketrans(string.punctuation,' '*len(string.punctuation))
    text = text.translate(translator)
    word_lst = text.split()
    return word_lst
    
def word_frequency(words_ls):
    """接收元素为单词的列表，统计每个单词出现的次数，根据出现次数排序，输出出现频率最高的50个单词及其出现次数
    以单词为字典的键，以单词出现次数为字典的值，遍历列表，单词每出现一次词频增加1."""
    word_dict = {}
    for word in words_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict
    
if __name__ == '__main__':
    filename = './src/01_Who Moved My Cheese.txt'
    txt = read_file(filename)
    words_list = words_lst(txt)  # 单词列表
    # word_frequency(words_list)
    print(word_frequency(words_list))