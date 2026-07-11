A=[]
for x in range(10000):
    a=64**11-4**10+96-x
    sa=''
    while a:
        sa=str(a%4)+sa
        a//=4
    sm=0
    for i in sa:
        sm+=int(i)
    if sm==71:
        A.append(x)
print(min(A))