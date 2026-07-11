f=open('26_1395.txt')
S,N=map(int,f.readline().split())
data=[]
for l in f:
    data.append(int(l))
data.sort()
sm=0
for i in range(len(data)):
    if data[i]+sm<=S:
        sm+=data[i]
    else:
        print(i)
        break
itog=0
for el in data[2209:]:
    itog+=el
print(len(data[2209:]),itog)