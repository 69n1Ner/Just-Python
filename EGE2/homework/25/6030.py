from re import fullmatch

for n in range(129,10**8,129):
    if fullmatch(r'12[0-9]3[0-9]*46',str(n)):
        print(n,n//129)