f=open('../files/24_demo.txt')
stroka=f.readline()
mx=0
k=0
for i in range(len(stroka)-1):
    if stroka[i]!=stroka[i+1]:
        k+=1
    else:
        k+=1
        mx=max(mx,k)
        k=0
print(mx)