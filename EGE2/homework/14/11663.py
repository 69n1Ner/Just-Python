alp=sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
dict={}
for i in range(len(alp)):
    dict[alp[i]]=i

mx=0
for x in alp[:27]:
    a=int('17'+x+'35',27)
    b=int(x+'742M',27)
    c=dict[x]**3  #
    w=a+b+c
    if w%23==0:
        print(x,w)
        mx=max(mx,int(x,27))
mx=str(mx)
a=int('17'+mx+'35',27)
b=int(mx+'742M',27)
c=int(mx,27)**3
w=a+b+c
print(int(str(w//23),27))
