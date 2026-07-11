f=open('../files/24_20909.txt').readline()
k=0
h=0
mx=0
for i in range(1,len(f)):
    if f[i]=='B' and f[i-1]=='A':
        k+=1
    while k>100:
        if f[h]+f[h+1]=='AB':
            k-=1
        h+=1
    if k==100:
        mx=max(mx,i-h+1)
print(mx)
