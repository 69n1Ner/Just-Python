f=open('../../files/24_16333.txt').readline()
mx=k=1

for i in range(1,len(f)):
    if (f[i].isdigit() and f[i-1].isdigit()) or \
            (f[i].isalpha() and f[i-1].isalpha()):
        k=1
    else:
        k+=1
    mx=max(mx,k)
print(mx)
