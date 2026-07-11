def f(x):
    P=25<=x<=73
    Q=75<=x<=118
    A=a1<=x<=a2
    return (A and (not Q))<=(P or Q)
r=[]
d=[y for x in (25,73,75,118) for y in (x,x+0.1,x-0.1)]
for a1 in d:
    for a2 in d:
        if a2>=a1 and all(f(x) for x in d):
            r+=[a2-a1]
print(round(max(r)))