f=open('26.2_19727.txt')
#как с коробками искать количество
#подставлять вместо наименьшего бидона остальные числа
M,N=map(int,f.readline().split())
mas=[int(i) for i in f]
mas.sort()
dat=[]
for el in mas:
    if sum(dat)+el<=M:
        dat.append(el)
print(len(dat))
del dat[-1]
mas.sort(reverse=True)
k=0
for el in mas:
   if sum(dat)+el>M:
       k+=1
print(k)
# obr1=mas[:161]
# #print(mas.index(30))
# obr2=set(mas[163:])
# obr2=list(obr2)
# for i in range(1,len(obr2)):
#
#     obr1.append(obr2[i])
#     if sum(obr1)>M:
#         print(obr2[i-1]) # последний объем, который увезет
#         break
#     obr1.remove(obr2[i])
# k=0
# for el in mas:
#     if el>43:
#         k+=1
# print(k)



