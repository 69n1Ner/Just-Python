f=open('26_4308.txt')
N=f.readline()
dic=dict()

for i in range(int(N)):
    row,col=map(int,f.readline().split())
    dic[row]=dic.get(row,[])+[col]
mx_col=0
mx_row=0
for row in sorted(dic):
    dic[row].sort()
    if len(dic[row])<2:
        continue
    for i in range(0,len(dic[row])-1):
        if dic[row][i+1]-dic[row][i]==2 and \
                dic[row][i]-1 not in dic[row] and \
                dic[row][i+1]+1 not in dic[row]:
            if dic[row][i+1]>mx_col:
                mx_row=row
                mx_col=dic[row][i+1]
print(mx_row,mx_col)
            # print(row,dic[row][i],dic[row][i+1])
