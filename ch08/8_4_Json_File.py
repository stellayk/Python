import json
user={'id':1234, 'name':'Python'}
print(type(user))
print(user['name'])

#json encoding
jsonString=json.dumps(user, ensure_ascii=False)

print(jsonString)
print(type(jsonString))

#json decoding
pyObj=json.loads(jsonString)
print(type(pyObj))

print(pyObj['name'])
for key in pyObj:
    print(key, ':', pyObj[key])


file=open("../examples/usagov_bitly.txt", mode='r', encoding='utf-8')
lines=file.readlines()

rows=[ json.loads(row) for row in lines]
print('rows: ', len(rows))

for row in rows[:10]:
    print(row)
    print(type(row))
file.close()

import pandas as pd
record_df=pd.DataFrame(rows)
print(record_df.info())