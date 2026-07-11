from itertools import permutations, product, repeat

k=0
for w in product('ДДИИДИ',repeat=5):
    if w[0]!="И" and w[-1]!="Д":
        k+=1
        print(w)
print(k)