alp=sorted('qwertyuiopasdfghjklzxcvbnm1234567890')
A=[]
for x in alp[:16]:
    a=int('11'+x+'73',16)
    b=int('94662'+x+'53'+x,16)
    c=int('6'+x+'41',16)
    d=int('31'+x+'77',16)
    e=int('9'+x+'82'+x+x+'181',16)
    exp=a+b+c+d+e
    if exp%15==0:
        A.append(exp//15)
print(min(A))