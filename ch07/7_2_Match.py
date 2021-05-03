from re import match
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)

if result:
    print('matched')
else:
    print('error')

jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)

if result:
    print('matched')
else:
    print('error')