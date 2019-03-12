# !usr/bin/env python
# -*- coding:utf-8 -*-
# Author:LiuQian,time:2019/3/11

import nltk

# nltk.download()

from bs4 import BeautifulSoup

import urllib.request

from nltk.corpus import stopwords


# 使用urllib模块来抓取web页面
response = urllib.request.urlopen('http://php.net/')
html = response.read()
print(html)
print('==========================================================================='
      '===========================================================================')


# BeautifulSoup模块来清洗这样的文字,这需要安装html5lib模块
soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)
print(text)
print('==========================================================================='
      '===========================================================================')


# 将文本转换为tokens
tokens = text.split()
print(tokens)
print('==========================================================================='
      '===========================================================================')


# 处理停用词——NLTK自带了许多种语言的停用词列表,from nltk.corpus import stopwords
clean_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)


# 使用Python NLTK统计token的频率分布,通过调用NLTK中的FreqDist()方法实现
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
print('==========================================================================='
      '===========================================================================')


# 如果搜索输出结果，可以发现最常见的token是PHP,可以调用plot函数做出频率分布图
freq.plot(20, cumulative=False)