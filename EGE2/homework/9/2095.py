f=open('../../files/2095.txt')
k=0
for l in f:
    line=l.split()
    if (line[0]==line[1] and line[2]!=line[0]) or \
            (line[0] == line[2] and line[1] != line[0]) or \
            (line[1] == line[2] and line[0] != line[1]):
        k+=1
print(k)