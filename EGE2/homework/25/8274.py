from re import finditer, fullmatch

for n in range(111,10**7,111):
    reg=r'22[0-9]0[0-9]*5[0-9]'
    if fullmatch(reg,str(n)):
        print(n,n//111)