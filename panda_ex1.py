import random
import pandas
d ={}
for n in range(5):
    d[f"level{ n}"]=[random.randint(5, 25), n]
    
print(d)
d["level6"]="New"
d['level0']=50
print(d)
l= pandas.DataFrame(d.items())
l.columns=['name', 'value',]
l=l.set_index('name')
print(l)
print(l.iloc[3][0][1])
print(l.index[3])
print(10 + True)
