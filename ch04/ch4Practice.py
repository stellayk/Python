position=['deputy manager','manager','representative','president','representative','deputy manager']
sposition=set(position)
lposition=list(sposition)
print('Nonduplicative Positions: ',lposition)

wc={}
for key in position:
    wc[key]=wc.get(key,0)+1
print('Frequency of each position: ',wc)