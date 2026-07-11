f=open('26_21424.txt')
N=f.readline()
mas=[]
for line in f:
    mas.append(int(line))
mas=sorted(mas,reverse=True)
mx=mas[0]
cor=[mx]
for el in mas[1:]:
    if (mx-el)>=9:
        mx=el
        cor.append(el)
print(len(cor),cor[-1])