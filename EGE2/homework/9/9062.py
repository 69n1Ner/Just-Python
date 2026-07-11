f=open('../../files/9062.txt')
k=0
for l in f:
    line=f.readline().split()
    if (line[0]!=max(line) or line[0]!=min(line)) and \
            (line[-1] != max(line) or line[-1] != min(line)):
        if abs(int(line[0])-int(line[-1]))!=0 and (int(max(line)) - int(min(line))) % (int(line[0]) - int(line[-1])) ==0:
            k+=1
print(k)