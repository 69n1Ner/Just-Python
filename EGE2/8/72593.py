from itertools import product
k=0
A= list(product('01*',repeat=8))

for w in A:
    S=''.join(w)

    if S[0]!='0' and S.count('0')==2 and S.count('*')<=4:
        k+=1
print(k)