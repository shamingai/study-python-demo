# -*- coding: utf-8 -*- 
# @Time : 2020/7/19 1:54 AM 
# @Author : zhaotong 
# @File : 17.jieba.py

import jieba

# Chinese
import jieba
txt = open("threekingdoms.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


#
# # English
# def getText():
#     txt = open("hamlet.txt", "r").read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
#         txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
#     return txt
#
#
# hamletTxt = getText()
# words = hamletTxt.split()
# counts = {}
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10}{1:>5}".format(word, count))



## test
# txt = "中国是一个伟大的国家"
# s = jieba.lcut(txt)
# print(s)
# s2 = jieba.lcut_for_search(txt)
# print(s2)
# s3 = jieba._lcut_for_search_no_hmm(txt)
# print(s3)