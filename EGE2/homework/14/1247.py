x=729**8-3**18+85
s=''
while x:
    s=str(x%9)+s
    x//=9
print(s.count('0'))
