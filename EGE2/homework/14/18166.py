k=0
xm=0
for x in range(2,2026):
    a = 5 ** 2025 + 5 ** 200 - x
    sx=''
    xc=a
    while xc:
        sx=str(xc%5)+sx
        xc//=5
    if sx.count('4')>=k:
        xm=x
        k=sx.count('4')
print(xm)