f=open('../../files/17_2014.txt')
mas=[int(i) for i in f]
k=0
def per(n,c):
    s=''
    while n:
        s = str(n % c) + s
        n //= c
    return int(s)
mx=-1
for el in mas:
    ch5=per(el,5)
    ch9=per(el,9)
    ch8=per(el,8)
    if ch5%10==3 and ch9%10==5 and ch8%10!=7:
        k+=1
        mx=max(mx,el)
print(k,mx)