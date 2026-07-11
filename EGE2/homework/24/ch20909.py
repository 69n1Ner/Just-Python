# from re import finditer
#
f=open('../../files/24_20909 (1).txt').readline()
# reg=r'[AB]*[A-F]*[AB]*'
# s=[x.group() for x in finditer(reg,f)]
# print(s)
l=0
k=0
mx=0
for r in range(1,len(f)):
    if f[r-1] + f[r]=='AB':
        k+=1
    if k>100:
        if f[l]+f[l+1]=="AB":
            k-=1
        l+=1
    if k==100:
        mx=max(mx,r-l+1)
print(mx)