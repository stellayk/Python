from re import sub
st3 = 'test^ABC abc KR*KR 123$tbc'
text1 = sub('[\^*$]+', '', st3)
print(text1)

text2 = sub('[a-zA-Z]', '', text1)
print(text2)