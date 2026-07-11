f=open('../../files/17_17873.txt')
mas=[int(i) for i in f]
mn=min(mas)
mx=0
k=0
for i in range(len(mas)-1):
    if mas[i]%16==mn or mas[i+1]%16==mn:
        k+=1
        mx=max(mx,mas[i]+mas[i+1])
print(k,mx)