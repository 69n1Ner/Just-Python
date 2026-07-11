from itertools import combinations
def f(x):
    P=24<=x<=77
    Q=47<=x<=92
    R=82<=x<=116
    A=a1<=x<=a2
    return (not( Q<=(P or R) ))<=((not(A)) <= (not(Q)) )
mas = [i/4 for i in range(24*4,116*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(min(ans))