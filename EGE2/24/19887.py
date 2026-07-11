f=open('../files/24.23_19887.txt').readline()
mx=0
l=0
for i in range(len(f)-1):
    if (int(f[i])%2)!=(int(f[i+1])%2):
        l+=1
    else:
        l+=1
        mx=max(mx,l)
        l=0
print(mx)