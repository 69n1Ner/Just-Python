from re import finditer

f=open('../../files/24_13085.txt').readline()
s=max(len(x.group()) for x in finditer(r'[A-WZ]*X[A-WZ]*Y[A-WZ]*|[A-WZ]*Y[A-WZ]*X[A-WZ]*',f))
print(s)
# for el in s:
#     if el!='':
#         print(el)