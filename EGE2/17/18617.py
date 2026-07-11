f=open('../files/17_18617.txt')
mas=[int(i) for i in f]
delM=max(mas)%3
delm=min(mas)%7
k=0
mx=-10**9
for i in range(len(mas)-1):
    if mas[i]%3==delM or mas[i+1]%3==delM:
        if mas[i]%7==delm or mas[i+1]%7==delm:
            k+=1
            mx=max(mx,mas[i]+mas[i+1])
print(k,mx)