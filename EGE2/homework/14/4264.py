x=9**11*3**20-3**9-27
s=''
while x:
    s=str(x%3)+s
    x//=3
print(s.count('2'))