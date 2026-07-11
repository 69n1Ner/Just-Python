alp = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for x in alp[:15]:
    a=int(x+'b09',17)
    b=int(x+'8e8',15)
    if (a+b)%155==0:
        print((a+b)//155)
