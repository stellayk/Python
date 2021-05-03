weigh = int(input("How much does your luggage weigh?"))
if weigh>=10:
    num = weigh // 10
    print('The fee is', 10000*num, 'won.')
else:
    print('There is no fee.')



import random
print('>>number guessing game<<')
com = random.randint(1,10)
while True:
    my = int(input('Enter a number:'))
    if my==com:
        print('correct!')
        break
    elif my>com:
        print('Enter a smaller number.')
    elif my<com:
        print('Enter a larger number.')




for n in range(3, 100, 6):
    print(n, end=' ')
sum = sum(range(3, 100, 6))
print('sum: ', sum)



multiline = """Hello. Welcome to the
Python world.
Python is an attractive language like a python."""

sents = []
words = []
for sen in multiline.split(sep = "\n"):
     sents.append(sen)
     for word in sen.split():
         words.append(word)

for w in words:
    print(w)
print('words count: ', len(words))