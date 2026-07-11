
f=open('../../files/17_9993.txt')
mas=[int(i) for i in f]
mx=-10**9
for el in mas:
    if el%100==17:
        mx=max(mx,el)
k=0
mx_pr=-10**9
def isprime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    return False


for i in range(1,len(mas)):
    if isprime(mas[i])== (not isprime(mas[i-1])):
        if (mas[i]+mas[i-1])%mx==0:
            k+=1
            mx_pr=max(mx_pr,mas[i]*mas[i-1])
print(k,mx_pr)
