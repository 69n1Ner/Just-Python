f=open('../../files/1962.txt')
k=0
for l in f:
    line=list(map(int,l.strip().split()))
    # if max(line)<=(sum(line)-max(line)):
    if (int(line[0])<(int(line[1])+int(line[2]))) and \
            (line[1] < (line[0] + line[2])) and \
            (line[2]<(line[1]+line[0])):
        k+=1
print(k)

