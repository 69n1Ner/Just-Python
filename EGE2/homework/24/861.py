from re import finditer

f=open('../../files/24_861.txt').readline()
s=[x.group() for x in finditer(r'SOCKCOS',f)]
print(len(s))