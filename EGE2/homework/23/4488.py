def f(x,y):
   if x==y:
       return 1
   if x>y:
       return 0
   if x%2==0:
       return f(x+1,y) + f(x+2,y) + f(x*2,y)
   else:
       return f(x*2,y)
print(f(1,32))