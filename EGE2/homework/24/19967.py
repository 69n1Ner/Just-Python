from re import finditer

f=open('../../files/24_19967.txt').readline()
reg1=r'([1-9][0-9]*|0)'
reg2=rf'AFD{reg1}([+*]{reg1})+'
s=max([x.group() for x in finditer(reg2,f)],key=len)
print(len(s),s)
