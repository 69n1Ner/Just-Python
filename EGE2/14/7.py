alp = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
for x in alp[:19]:
    a=int('78'+x+'79643',19)
    b=int('25'+x+'43',19)
    c=int('63'+x+'5',19)
    if (a+b+c)%18==0:
        print((a+b+c)//18)