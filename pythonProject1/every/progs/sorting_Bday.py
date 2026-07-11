f=open('../files/Текстовый документ.txt')
data=[]
for l in f:
    data.append(l.strip())
data.sort()
print(data)
print('19' in data)
print(len(data))