x=49**7+7**20-28
s=''
while x:
    s+=str(x%7)
    x//=7
print(s.count('6'))
