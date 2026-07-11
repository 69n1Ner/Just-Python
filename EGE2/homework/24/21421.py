from re import fullmatch, finditer, match

f=open('../../files/24_21421.txt').readline()
k=0
# match=finditer(r'[123456789AB][0123456789AB]*[02468A]',f)
# for el in match:
#     print(el[0])


s=max([x.group() for x in finditer(r'[123456789AB][0123456789AB]*[02468A]',f)],key=len)
print(len(s),s)