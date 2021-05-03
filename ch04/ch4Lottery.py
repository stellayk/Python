import random
lottery = []
for i in range(0,6):
    num = random.randint(1,46)
    while num in lottery:
        num = random.randint(1,46)
    lottery.append(num)
lottery.sort()

userNums = []
for x in range(0,6):
    choice = int(input("Choose a number 1 through 45: "))
    if 1 <= choice <= 45:
        userNums.append(choice)
    else:
        choice = int(input("Invalid number. Choose a number 1 through 45: "))
        userNums.append(choice)
print("Your choice of numbers are", userNums)

count=0
for userNums in lottery:
    if userNums in lottery:
        count += 1

print("Today's lottery numbers are", lottery)

if count==6:
    print("Congrats! You won a jackpot!")
elif count==4:
    print("You won a third place")
elif count==3:
    print("You won a fourth place")
else:
    print("Try next time...")




# 1st 6 nums
# no 2nd place
# 3rd 4
# 4th 3