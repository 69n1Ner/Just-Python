from itertools import combinations, permutations


def f(x):
    P=25<=x<=240
    Q=175<=x<=300
    R=270<=x<=340
    A=a1<=x<=a2
    return ( (Q)<=(P) )or( (not A)<=(R) )
mas=[i/4 for i in range(100*4,340*4+1)]
ans=[]
for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(min(ans))
print(ans)