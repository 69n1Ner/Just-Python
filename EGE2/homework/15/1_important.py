from itertools import combinations, permutations


def f(x):
    P=10<=x<=25
    Q=15<=x<=30
    R=25<=x<=40
    A=a1<=x<=a2
    return ((Q)<=(not(R))) and (A) and (not P)
mas = [i/4 for i in range(10*4,40*4+1)]
ans=[]

for a1,a2 in permutations(mas,2):
    if all(f(x)==0 for x in mas):       #ВАЖНО
        ans.append(a2-a1)
print(max(ans))