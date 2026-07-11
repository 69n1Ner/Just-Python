f=open('26_6056.txt')
N=int(f.readline())
mas=[]
ans=[]
for line in f:
    mas.append(int(line))
mas.sort(key=lambda x: -x)
mx=mas[0]
del(mas[0])
for el in mas:
    if mx-el>=56:
        mx=el
        ans.append(el)
print(len(ans)+1,min(ans))
