x=8**1006+5**1947+505
s=''
while x:
    s=str(x%7)+s
    x//=7
print(s.count('6')*6-s.count('2')*2)