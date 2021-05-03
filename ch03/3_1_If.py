score = int(input('Enter your score: '))
if score>=85 and score<=100 :
     print('Excellent')
else :
     if score>=70 :
         print('Average')
     else :
         print('Not efficient')


score = int(input('Enter your score: '))
grade = ' '
if score>=85 and score<=100 :
    grade = 'Excellent'
elif score>=70 :
    grade = 'Average'
else :
    grade = 'Not efficient'
print('Your score is %d, and your grade is %s' %(score,grade))



cnt = tot = 0
while cnt <5 :
    cnt +=1
    tot +=cnt
    print(cnt, tot)