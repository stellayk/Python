name=['Tom', 'Michelle', 'Brandon']
print('name address=', id(name))

name2=name
print('name2 address=', id(name2))

print(name)
print(name2)

import copy
name3=copy.deepcopy(name)
print(name)
print(name3)
print('name3 address=', id(name3))