for x in range(9):
    for y in range(9):
        a= int('88'+str(x)+'4'+str(y),9)
        b=int('7'+str(x)+'44'+str(y),11)
        if (a+b)%61==0:
            print((a+b)//61)