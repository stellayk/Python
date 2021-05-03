string = "abc"
print(len(string))
for s in string :
    print(s)

lstset = [1,2,3,4,5]
for e in lstset:
    print('e: ', e)


i=0
while i<10:
    i +=1
    if i==3:
        continue
    if i==6:
        break
    print(i, end=' ')


num1 = range(10)
print('num1: ', num1)
num2 = range(1, 10)
print('num2: ', num2)
num3 = range(1, 10, 2)
print('num3: ', num3)

for n in num1:
    print(n, end=' ')
print()
for n in num2:
    print(n, end=' ')
print()
for n in num3:
    print(n, end=' ')
print()


import random
lst = []
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)

print('lst=', lst)

for i in range(10):
    print(lst[i]*0.25)
#comprehension [expression for item in list]
a = [random.randint(1,10)*0.25 for x in range(10)]
print(a)



for i in range(2,10):
    print('~~~{}~~~'.format(i))

    for j in range(1,10):
        print('%d * %d = %d'%(i, j ,i*j))


string = """I love burgers.
Chick-fil-a is the best one.
Do you like it too?"""

sents = []
words = []

for sen in string.split(sep = "\n"):
    sents.append(sen)
    for word in sen.split():
        words.append(word)

print('sentence: ',sents)
print('no of sentence: ', len(sents))
print('word: ', words)
print('no of word: ', len(words))
