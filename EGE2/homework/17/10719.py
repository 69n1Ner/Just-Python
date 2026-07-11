f=open('../../files/17_10719.txt')
mas=[int(i) for i in f]
k=0
mx=-10**9
for i in range(len(mas)-3):
    if ( abs(mas[i])%100==13 ) != ( abs(mas[i+3])%100==13 ):
        k+=1
        mx=max(mx,mas[i]+mas[i+3])
print(k,mx)