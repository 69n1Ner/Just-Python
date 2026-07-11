for x in range(7):
    for y in range(7):
        a=int(str(y)+str(x)+'320',7)
        b=int('21424'+str(x)+'3'+str(y)+'3',9)
        if (a+b)%181==0:
            print((a+b)//181)
