from itertools import product, repeat
k=0
for w in product('012345678',repeat=6):
    s=''.join(w)

    if s[0]!='0' and s.count('4')==1 and (s.count('21424')+s.count('3')+s.count('5')+s.count('7'))==2:
        k+=1
print(k)