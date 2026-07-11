x=4**625 - 2**311 + 2**571 -48
s=''
while x:
    s=str(x%4)+s
    x//=4
print(s.count('21424'))