cnt = tot = 0
while cnt <5 :
    cnt +=1
    tot +=cnt
    print(cnt, tot)

cnt = tot = 0
dataset=[]
while cnt<100 :
    cnt +=1
    if cnt%3==0 :
        tot +=cnt
        dataset.append(cnt)

print('%d' %tot)
print('dataset =', dataset)




numData = []
while True:
    num=int(input("Enter a number: "))

    if num%10==0 :
        print("Exit")
        break
    else:
        print(num)
        numData.append(num)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while True:
    print("Select an operator. 1.Add 2.Subtract 3.Multiply 4.Divide 0.Exit")
    op = input("Enter your choice of operator: ")

    if op == '1':
        print(num1, "+", num2, "=", num1+num2)
    elif op == '2':
        print(num1, "-", num2, "=", num1-num2)
    elif op == '3':
        print(num1, "*", num2, "=", num1*num2)
    elif op == '4':
        print(num1, "/", num2, "=", num1/num2)
    elif op == '0':
        print("Program ended")
        break
    else:
        print("Invalid")