k=0
f=open('../../files/2041.txt')
for l in f:
    line=f.readline().split()
    for i in range(len(line)-3):
        if line[0]<(line[1]+line[2]+line[3]) and \
                line[1] < (line[0] + line[2] + line[3]) and \
                line[2] < (line[1] + line[0] + line[3]) and \
                line[3] < (line[1] + line[2] + line[0]):
            k+=1
print(k)