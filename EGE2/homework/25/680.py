from itertools import count, combinations


def delit(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)

def is_prime(n):
    if n<2: return False
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return False
    return True
print(delit(487451))

for n in range(485_617,529_678+1):
    mas=delit(n)
    if len(mas)>=3:
        for a1,a2,a3 in combinations(mas,3):
            if a1!=a2 and a1!=a3 and a2!=a3:
                if is_prime(a1) and is_prime(a2) and is_prime(a3):
                    if (a1%10==a2%10==a3%10) and ((a1*a2*a3)==n):
                        if (max(a1,a2,a3)-min(a1,a2,a3))<100:
                            print(n,max(a1,a2,a3)-min(a1,a2,a3))
                            print(a1,a2,a3,a1*a2*a3)
                            print()
