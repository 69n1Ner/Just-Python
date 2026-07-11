from itertools import product, repeat
k=0
for w in product("ЛЮСТРА",repeat=5):
    s=''.join(w)
    if s.count('Ю')<=2 and s[-1]!="Л" and s[-1]!="С" and s[-1]!="Т" and s[-1]!="Р":
        k+=1
print(k)