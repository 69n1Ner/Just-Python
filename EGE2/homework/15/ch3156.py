from itertools import combinations
# def f(x):
#     P=2<=x<=20 and x%2==0
#     Q=5<=x<=50 and x%5==0
#     A=x and x==int(x)
#     return (A<=P)and(Q<= (not A))
# mas=[i for i in range(2,50+21424)]
# ans=[]
#
# for x in mas:
#     if all(f(x) for x in mas):
#         ans.append(x)
# print(ans)

P=[2,4,6,8,10,12,14,16,18,20]
Q=[x for x in range(5,50+1,5)]
A=[x for x in range(-100,100)]
for x in range(-100,100):
    if ((x in A)<=(x in P))and((x in Q)<= (not (x in A))):
        print(x)
