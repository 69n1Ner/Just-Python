from re import fullmatch

for n in range(2023,10**8,2023):
    if fullmatch(r'671[0-9][0-9]21424[0-9]*',str(n)):
        print(n,n//2023)