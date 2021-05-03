import random
dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

vmax=vmin=dataset[0]

for i in dataset:
    if vmax<i:
        vmax=i
    if vmin>i:
        vmin=i

print('max=', vmax, ' min=', vmin)


dataset=[5,10,18,22,35,55,75,103]
value=int(input("Enter: "))

low=0
high=len(dataset)
loc=0
state=False

while(low <= high):
    mid = (low+high)
    if dataset[mid] > value:
        high = mid-1
    elif dataset[mid] < value:
        low = mid+1
    else:
        loc = mid
        state = True
        break