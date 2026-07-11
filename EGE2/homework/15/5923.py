from functools import lru_cache
from itertools import combinations

@lru_cache
def f(x):
    P=5<=x<=280
    Q=295<=x<=400
    R=375<=x<=450
    A=a1<=x<=a2
    f=(Q<=P) or ((not A) <=R)
    return f
mas=[i/4 for i in range(5*4,450*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    fl=True
    for x in mas:
        if not f(x):
            fl=False
            break
    if fl:
        ans.append(a2 - a1)
    # if all(f(x) for x in mas):
    #     ans.append(a2-a1)
print(min(ans))
