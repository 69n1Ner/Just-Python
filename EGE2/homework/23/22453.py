def f(x,y):
    if x==y:
        return 1
    if x<y:
        return 0
    return f(x-2,y)+f(x-20,y)+f(x//3,y)
mas=[161]
for i in range(50,10+1,-1):
    if i%2!=0:
        mas.append(i)
mas.append(7)
res=1
for i in range(1,len(mas)):
    res*=f(mas[i-1],mas[i])
print(res)
