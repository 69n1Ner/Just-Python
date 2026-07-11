from itertools import product, combinations


def f(x):
    B=36<=x<=75
    C=60<=x<=110
    A=a1<=x<=a2
    return (not(A))<=(B==C)
mas=[i/4 for i in range(36*4,110*4+1)]
ans=[]
for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(min(ans))