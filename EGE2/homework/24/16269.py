# from re import finditer
#
f=open('../../files/24_16269.txt').readline()
# s=[x.group() for x in finditer(r'((XX|YY|ZZ){1})+',f)]
# for el in s:
#     if el!='':
#         print(el)
f=f.replace('T',' ').replace('U',' ').replace('V',' ').replace('W',' ')
for x in 'XYZ':
    while x*4 in f:
        f=f.replace(x*4,x*2+' '+x*2)
    while x*3 in f:
        f=f.replace(x*3,x*2+' '+x*2)
    f=f.replace(x*2,'*')
    f=f.replace(x,' ')
print(max(map(len,f.split()))*2)