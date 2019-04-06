from konlpy.tag import Okt
import re
#import nltk
#nltk.download()
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

okt = Okt()
ctx = "C:/Users/ezen/PycharmProjects/syyoo-2/data/"
filename = ctx + 'KakaoTalkChats2.txt'
filename2 = ctx + 'stopwords.txt'
font = ctx + "D2Coding.ttf";

with open(filename, 'r', encoding='UTF-8') as f:
    texts = f.read()
#print(texts[:300])

texts = texts.replace('\n', '')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('', texts)

tokens = word_tokenize(texts)

noun_token = []
for token in tokens:
    token_pos = okt.pos(token)
    temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == "Noun"]
    if len(''.join(temp)) > 1:
        noun_token.append("".join(temp))
texts = " ".join(noun_token)


with open(filename2, 'r', encoding='UTF-8') as f:
    stopwords = f.read()

stopwords = stopwords.split(' ')


texts = [text for text in tokens if text not in stopwords ]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
print(freqtxt[:30])


wcloud = WordCloud(font, relative_scaling=0.2, background_color='white').generate(" ".join(texts))
plt.figure(figsize=(140,80))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()