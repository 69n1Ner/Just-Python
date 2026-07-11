from itertools import combinations

def f(x):
    P= 5<=x<=30
    Q=14<=x<=23
    A=a1<=x<=a2
    return ((P)==(Q))<=(not(A))
mas = [i/4 for i in range(5*4,30*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(max(ans))