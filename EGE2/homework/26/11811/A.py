f=open('26_11811.txt')
N,R=map(int,f.readline().split())
data=[]
for l in f:
    data.append(list(map(int,l.split())))
data.sort(key=lambda x: (x[0],x[1]))
k=data[0][0]>1
mx=0
mn=data[0][0]
# for el in data:
#     if start<el[0]:
#         k+=1
#         start=el[1]
# if R-data[-1][1]!=0:
#     k+=1
# tmp=[]
# print(data)
# for i in range(1,len(data)):
#     if data[i-1][1]>=data[i][0]:
#         tmp.append([min(data[i-1][0],data[i][0]),max(data[i][1],data[i-1][1])])
# print(tmp)
# tmp=tmp[-1][1]-tmp[0][0]
# print(k,tmp)
mx_end=data[0][1]
for start,end in data[1:]:
    if start>mx_end:
        k+=1
        mn=start
    mx_end=max(mx_end,end)
    mx=max(mx,mx_end-mn)
print(k+(mx_end<R),mx)