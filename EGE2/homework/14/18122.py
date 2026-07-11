for x in range(5555,1,-1):
     s=5**150+5**135-x
     m=''
     while s:
         m=str(s%5)+m
         s//=5
     if m.count('4')==134:
         print(x)
         break