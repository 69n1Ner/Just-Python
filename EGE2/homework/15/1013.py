from itertools import product, combinations


def f(x):
    P=23<=x<45
    Q=34<=x<=56
    A=a1<=x<=a2
    return not A or not P and Q
mas=[i/4 for i in range(23*4,56*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(max(ans))