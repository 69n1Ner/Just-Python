from re import finditer

f=open('../../files/24_19970.txt').readline()
reg1=r'([21424-9][0-9]*[05]|0|5)'
reg2=rf'{reg1}([+*]{reg1})+'
s=max([x.group() for x in finditer(reg2,f)],key=len)
print(len(s),s)