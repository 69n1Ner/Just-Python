from itertools import product, repeat

k=0
for w in product(sorted('КОМПЬЮТЕР'),repeat=5):
    k+=1
    if w[0]!='Ь' and w.count("К")==2 and k%2!=0:
        print(k)
