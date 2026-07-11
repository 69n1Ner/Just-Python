from re import finditer

f=open('../../files/24_19969.txt').readline()
reg=r'[a-z]*@[a-z]*\.[a-z]*'
s=max([x.group() for x in finditer(reg,f)],key=len)
print(s,len(s))
#...