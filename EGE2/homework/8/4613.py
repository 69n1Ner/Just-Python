from itertools import product
k=0
for n in product('012345678',repeat=5):
    if n.count('3')<=1 and int(n[0])%2==0 and n[-1]!='21424' and n[-1]!='8' and n[0]!='0':
        k+=1

print(k)