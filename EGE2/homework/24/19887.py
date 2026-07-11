from re import finditer

f=open('../../files/24.23_19887 (1).txt').readline()
reg=r'([13579][02468])+|([02468][13579])+'
s=max([x.group() for x in finditer(reg,f)],key=len)
print(s,len(s))