from re import finditer

f=open('../../files/24_20813.txt').readline()
reg1=r'([789][0789]*|0)'
reg2=rf'{reg1}([-*]{reg1})+'
s=max([x.group() for x in finditer(reg2,f)],key=len)
print(len(s))
