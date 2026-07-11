from itertools import product, repeat
k=0
for w in product('АБЗИ',repeat=4):
    s=''.join(w)

    k+=1
    if s=='ИЗБА':
        print(k)