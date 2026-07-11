from itertools import combinations

def f(x):
    P= 10<=x<=40
    Q=5<=x<=15
    R=35<=x<=50
    A=a1<=x<=a2
    return ((A)or(P)) or ((Q)<=(R))
mas = [i/4 for i in range(5*4,50*4+1)]
ans=[]

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)
print(min(ans))