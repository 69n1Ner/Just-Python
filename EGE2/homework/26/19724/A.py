#1.- проверка на наличие элемента в ячейке
#2.+ сравнение времени окончания+1 и начала
#3.+ запись в ячейку
#4. если
f=open('26.17_19724.txt')
K=int(f.readline())
N=int(f.readline())
first=[]
slots=[[0,0] for x in range(K)]
for l in f:
    st,end=map(int,l.split())
    first.append([st,end])
first.sort()
k=0
num=0
for i in range(len(first)): # в общем списке
    if slots[-1]!=[0,0]:
        break
    for j in range(K): # в списке слотов
        if (first[i][0]-1)>=slots[j][1]:
            slots[j]=first[i]
            k+=1
            num=j+1
            break
print(slots[-1],first[229])
print(k,num)