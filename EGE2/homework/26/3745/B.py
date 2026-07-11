f=open('26_3745.txt')
mat=[[0 for x in range(10_002)] for y in range(10_002)]
n=f.readline()
k=0
for l in f:
    y,x=map(int,l.split())
    mat[y-1][x-1]=1
lines=[0]*10_001
for y in range(10_001-1):
    fly=True
    for x in range(10_001-1):
        flx=True
        if mat[y][x]!=1:
            continue
        if mat[y][x+1]==1 and mat[y+1][x]==1 and mat[y+1][x+1]==1:
            if y==0:
                fly=False
            if x==0:
                flx=False
            if flx and fly:# все стороны
                if mat[y][x-1] ==0 and mat[y-1][x]==0 and mat[y-1][x+1]==0\
                    and mat[y][x+2]==0 and mat[y+1][x+2]==0 and mat[y+2][x+1]==0\
                    and mat[y+2][x]==0 and mat[y+1][x-1]==0:
                    k+=1
                    lines[y]+=1
                    lines[y+1] += 1

            elif flx and not fly: # нельзя вверх
                if mat[y][x-1] ==0 \
                    and mat[y][x+2]==0 and mat[y+1][x+2]==0 and mat[y+2][x+1]==0\
                    and mat[y+2][x]==0 and mat[y+1][x-1]==0:
                    k+=1
                    lines[y] += 1
                    lines[y + 1] += 1

            elif not flx and fly: # нельзя влево
                if  mat[y - 1][x] == 0 and mat[y - 1][x + 1] == 0 \
                and mat[y][x + 2] == 0 and mat[y + 1][x + 2] == 0 and mat[y + 2][x + 1] == 0 \
                and mat[y + 2][x] == 0 :
                    k+=1
                    lines[y] += 1
                    lines[y + 1] += 1


            elif not flx and not fly: # нельзя вверх и влево
                if mat[y][x + 2] == 0 and mat[y + 1][x + 2] == 0 and mat[y + 2][x + 1] == 0 \
                and mat[y + 2][x] == 0 :
                    k+=1
                    lines[y] += 1
                    lines[y + 1] += 1


print(k,lines.index(max(lines))+1)
#
# for el in mat:
#     print(el)

