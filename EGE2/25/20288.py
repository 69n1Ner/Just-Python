from re import fullmatch
for i in range(9231,10**10+1,9231):
    if fullmatch(r'[02468]*12[13579]4[13579]',str(i)):
        print(i,i//9231)