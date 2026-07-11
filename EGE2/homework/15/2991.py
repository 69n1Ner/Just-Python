from itertools import product, combinations


def f(x):
    P=10<=x<=20
    Q=35<=x<=45
    A=a1<=x<=a2
    return ((not(P))<=Q)and(not(A))
mas=[i/4 for i in range(10*4,45*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x)==0 for x in mas):
        ans.append(a2-a1)
print(min(ans))