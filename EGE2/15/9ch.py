from itertools import combinations

def f(x):
    P= 130<=x<=171
    Q=150<=x<=185
    A=a1<=x<=a2
    return P<=((Q and (not(A))) <= (not(P)))
mas = [i/4 for i in range(130*4,185*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(min(ans))