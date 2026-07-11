from re import finditer

f=open('../../files/24_6757.txt').readline()
f=f.replace('CFE','*').replace('FCE','*')
for x in 'FCED':
    f=f.replace(x,' ')
print(max(map(len,f.split())))
