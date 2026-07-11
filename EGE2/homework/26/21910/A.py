f=open('26_21910.txt')
f.readline()
data=set()
for l in f:
    dl=int(l)
    data.add(dl)
data=list(sorted(data,key=lambda x:-x))
print(data)
k=1 # <--- не 0, а 1
first=data[0]# потому, что тут есть уже элемент
for i in range(1,len(data)):
    if first-data[i]>=9:
        first=data[i]
        k+=1
print(k,first)
