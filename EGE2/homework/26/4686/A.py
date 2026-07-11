from re import *
f=open('26_4686.txt')
data=[]
N,M=map(int,f.readline().split())
for l in f:
    x,y=map(int,l.split())
    data.append([x,y])
data.sort()
building=[[0]*5000 for x in range(2000)]
for el in data:
    building[el[0]-1][el[1]-1]=1
reg=r'(1)*(0)(1)*'
pat=compile(reg)
co=0
mx=0
for el in building:
    s=''.join(map(str,el))
    last=s.rfind('1')
    if last==-1:
        continue
    # v=[x.group() for x in pat.finditer(s)]
    # print(v[:10],s[:100])
    # break
    for m in finditer('0',s[:last+1]):
        i =m.start()
        l=search(r'1*$',s[:i]).group()
        r=search(r'^1*',s[i+1:]).group()
        b=l+'0'+r
        if b.count('1')>=M:
            co+=1
            mx=max(mx,building.index(el)+1)
print(co,mx)