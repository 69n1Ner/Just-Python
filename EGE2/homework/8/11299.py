from itertools import permutations, repeat, combinations, product
k=1
s=sorted('БМЮРН')
for w in product(s,repeat=6):
    k+=1
    if k%2!=0 and w[0]!='М' and w.count('Р')>=2 and w.count('Ю')==0:
        print(w,k)