f=open('26_21719.txt')
N=f.readline()
s=set()
for l in f:
    x,y=map(int,l.split())
    s.add((x,y))
s=list(sorted(s))
data=[[] for x in range(1_000_000)]
for el in s:
    x=el[0]
    y=el[1]
    data[x].append(y)

# for i,el in enumerate(data):
#     if len(el)>=20:
#         print(i,el,len(el))


counter=[0]*len(data)
for i in range(0,len(data)):
    if len(data[i])>=2:
        nums=set()
        mx=0
        for j in range(1,len(data[i])):
            if data[i][j]-data[i][j-1]==2:
                nums.add(data[i][j])
                nums.add(data[i][j-1])
            else:
                mx=max(len(nums),mx)
                nums=set()
        counter[i]+=mx

for i,el in enumerate(counter):
    if el!=0:
        print(i,el)
        break