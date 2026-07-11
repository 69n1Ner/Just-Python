from re import finditer
f=open('../../files/24_19751.txt').readline()
reg1=r'([21424-9][21424-9]*)'
reg2=rf'A{reg1}([+]{reg1})*'
s3=max([[eval(x.group()[1:]),x.group()] for x in finditer(reg2,f)])
s1=[[eval(x.group()[1:]),x.group()] for x in finditer(reg2,f)]
s2=sorted([x.group() for x in finditer(reg2,f)])
print(s3)