alp=sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for x in alp[:21]:
    a=int('82934'+x+'2',21)
    b=int('2924'+x+x+'7',21)
    c=int('67564'+x+'8',21)
    s=a+b+c
    if s%20==0:
        k=s//20
        print(k)

        break