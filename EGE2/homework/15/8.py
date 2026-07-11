from itertools import combinations
def f(x):
    C=48<=x<=94
    J=83<=x<=100
    A=a1<=x<=a2
    return (not((C)or(J)))<=(not(A))
mas=[i/4 for i in range(48*4,100*4+1)]
ans=[]
for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(max(ans))