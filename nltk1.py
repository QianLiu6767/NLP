# !usr/bin/env python
# -*- coding:utf-8 -*-
# Author:LiuQian,time:2019/3/11


# ------------------使用句子tokenizer将文本tokenize成句子:--------------------------------
from nltk.tokenize import sent_tokenize

mytext1 = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext1))

mytext2 = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext2))


# ---------------------------单词tokenizer--------------------------------
# Mr.这个词也没有被分开。
# NLTK使用的是punkt模块的PunktSentenceTokenizer，它是NLTK.tokenize的一部分。
# 而且这个tokenizer经过训练，可以适用于多种语言
from nltk.tokenize import word_tokenize

mytext3 = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(word_tokenize(mytext3))


# -------------------------------非英文Tokenize，Tokenize时可以指定语言-----------------------------
from nltk.tokenize import sent_tokenize

mytext4 = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(mytext4, "french"))


# --------------同义词处理：使用nltk.download()安装界面，其中一个包是WordNet。
# -------------WordNet是一个为自然语言处理而建立的数据库。它包括一些同义词组和一些简短的定义---------------
from nltk.corpus import wordnet

syn = wordnet.synsets("pain")
print("Definition-pain:", syn[0].definition())
print("Example-pain:", syn[0].examples())

syn1 = wordnet.synsets("NLP")
print("Definition-NLP:", syn1[0].definition())
syn2 = wordnet.synsets("Python")
print("Definition-Python:", syn2[0].definition())

# 使用WordNet来获取同义词
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

# 使用WordNet来得到反义词
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)


# -------------------------------------词干提取--------------------------
# 语言形态学和信息检索里，词干提取是去除词缀得到词根的过程，例如working的词干为work。
# 搜索引擎在索引页面时就会使用这种技术，所以很多人为相同的单词写出不同的版本。
# 有很多种算法可以避免这种情况，最常见的是波特词干算法。NLTK有一个名为PorterStemmer的类，就是这个算法的实现
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('working'))
print(stemmer.stem('worked'))

# 非英文词干提取:除了英文之外，SnowballStemmer还支持13种语言-
from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)

# 使用SnowballStemmer类的stem函数来提取像这样的非英文单词
french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("French word"))


# --------------------------------单词变体还原------------------------------------
# 变体还原的结果是一个真实的单词。不同于词干，当你试图提取某些词时，它会产生类似的词

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print(stemmer.stem('increases'))

# 如果用NLTK的WordNet来对同一个单词进行变体还原，才是正确的结果
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('increases'))

# 结果可能会是一个同义词或同一个意思的不同单词。
# 有时候将一个单词做变体还原时，总是得到相同的词。
# 这是因为语言的默认部分是名词。要得到动词，可以这样指定
# 动词(v)、名词(n)、形容词(a)或副词(r)
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('playing', pos="v"))
print(lemmatizer.lemmatize('playing', pos="n"))
print(lemmatizer.lemmatize('playing', pos="a"))
print(lemmatizer.lemmatize('playing', pos="r"))
print('===============================================================')

# ------------------词干和变体的区别-------------------
# 词干提取不会考虑语境，这也是为什么词干提取比变体还原快且准确度低的原因
# 个人认为，变体还原比词干提取更好。单词变体还原返回一个真实的单词，即使它不是同一个单词，也是同义词，但至少它是一个真实存在的单词。
# 如果你只关心速度，不在意准确度，这时你可以选用词干提取。
# 在此NLP教程中讨论的所有步骤都只是文本预处理。在以后的文章中，将会使用Python NLTK来实现文本分析。
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print(stemmer.stem('stones'))
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jokes'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purple'))
print('----------------------')
print(lemmatizer.lemmatize('stones'))
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))