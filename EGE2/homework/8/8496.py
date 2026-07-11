from itertools import product

for i,w in enumerate(product('АВОРТ',repeat=6),start=1):
    w=''.join(w)
    if w=='ВОРОТА':
        print(i)