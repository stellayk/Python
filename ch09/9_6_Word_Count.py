import pickle
file=open("data.pickle", mode='rb')
news_data2=pickle.load(file)

import re
def clean_text(text_string):
    text_string_re = re.sub('[,.?!:\'\";]','',text_string)
    text_string_re = re.sub('[!@#$%^&*()]|[0-9]','', text_string_re)
    text_string_re = text_string_re.lower()
    text_string_re = re.sub('[a-z]','',text_string_re)
    text_string_re = ' '.join(text_string_re.split())
    return text_string_re

clean_texts = [clean_text(row) for row in news_data2]
print(clean_texts)

word_count={}
for text in clean_texts:
    for word in text.split():
        word_count[word]=word_count.get(word,0)+1
print(word_count)

del word_count['[바로잡습니다]']

new_word_count={}
for word, cnt in word_count.items():
    if cnt >=3 and len(word) >=2 and len(word) <= 3:
        print(word, '->', word_count[word])
        new_word_count[word]=new_word_count.get(word, cnt)
print(new_word_count)

from collections import Counter

counter = Counter(new_word_count)
top5_word = counter.most_common(5)
print(top5_word)


#graphs
words=[]
counts=[]

for word, count in top5_word:
    words.append(word)
    counts.append(count)
print(words)
print(counts)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.plot(words,counts)
plt.show()

plt.bar(words,counts)
plt.show()