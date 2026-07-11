f=open('26_20815.txt')
n,k=map(int,f.readline().split())
m_all=[]
mins_279=[]

for line in f:
    ida,p1,p2,p3,sob=map(int,line.split())
    m_all.append([p1+p2+p3+sob,ida,p1,p2,p3,sob])
    if p1+p2+p3+sob==279:
        mins_279.append([sob,ida,p1,p2,p3])
mx=0
co=0
for el in m_all:
    if el[0]==280:
        mx = max(mx, el[1])
    if el[0]==279:
        co+=1
print(mx,co)


m_all.sort(reverse=True)
mins_279.sort(reverse=True,key=lambda x: (x[0],x[1]))
itog=[x for x in m_all if x[0]>279]
itog.sort(reverse=True,key=lambda x: (x[0],x[-1],x[1]))

for el in itog:
    print(el)

k_279=k-len(itog)
for i in range(k_279):
    itog.append([279,mins_279[i][1],mins_279[i][2],mins_279[i][3],mins_279[i][4],mins_279[i][0]])

# for el in itog:
#     print(el)
