dic = dict(key1=100, key2=200, key3=300)
print(dic)

person={'name':'James Clark', 'age':35, 'address':'Colorado'}
print(person)
print(person['name'])
print(type(dic), type(person))
person['age']=45
print(person)
del person['address']
print(person)
person['pay']=350
print(person)

print(person['age'])
print('age' in person)
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)


charset=['abc','code','bets','virgin','galactic','abc','cirrus','logic','gamestop','stock','market','abc','logic','reddit','bets']
wc={}
for key in charset:
    wc[key]=wc.get(key,0)+1
print(wc)