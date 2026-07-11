from itertools import combinations

def f(x):
    P = 1 <= x <= 39 #
    Q = 23 <= x <= 58 #
    A = a1 <= x <= a2
    return ((P)<=(not(Q)))<= ((not(A))) #

mas = [i/4 for i in range(1*4, 58*4+1)] #
ans = []

for a1,a2 in combinations(mas,2):
    if all(f(x) for x in mas):
        ans.append(a2-a1)

print(max(ans)) #
