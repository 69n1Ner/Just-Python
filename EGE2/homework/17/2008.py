f=open('../../files/17_2008.txt')
mas=[int(i) for i in f]
k=0
mn=10**9
for i in mas:
    if int(str(i)[-2])<=4 and (3<=int(str(i)[-3])<=7):
        k+=1
        mn=min(mn,i)
print(k,mn)