from re import *
f=open('../../files/24_22447.txt')
test='GH012AKLFAS'
reg=r'(?=([1-9A-F][0-9A-F]*|[0]))'
#s=[x.group(1) for x in finditer(reg,test)]
mas=findall(r'[0-9A-F]+',f.readline())
k=0
for el in mas:
    for i in range(len(el)):
        for j in range(i+1,len(el)+1):
            s=el[i:j]
            if s=='0' or s[0]!='0':
                k+=1
print(k)
