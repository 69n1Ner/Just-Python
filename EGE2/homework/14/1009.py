from itertools import count

x=7**21+49**13-7**10
s=''
while x:
    s=str(x%7)+s
    x//=7
print(s.count('6'))