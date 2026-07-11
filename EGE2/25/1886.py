
for N in range(39345600,1,-(2*3*5*7)):
    k=0
    if N%2==0 and N%3==0 and N%5==0 and N%7==0:
        for d in range(2,int(N**0.5)+1):
            if N%d==0:
                k+=1 if d==N//d else 2  #
        if 88>=k>=76 :
            print(N,k)
