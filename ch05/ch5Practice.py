height = int(input('height: '))
starCount = 0

for x in range(1, height+1):
    print("* " * x)
    starCount += x

print(starCount)