from itertools import combinations
def f(x):
    P=6<=x<=17
    Q=13<=x<=28
    A=a1<=x<=a2
    return (A<=P)or(Q)
mas= [i/4 for i in range(6*4,28*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(max(ans))

