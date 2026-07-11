
for n in range(81234,134689+1):
    mas=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            mas|={d,n//d}
        if len(mas)>3:
            break
    if len(mas)==3:
        print(*sorted(mas))