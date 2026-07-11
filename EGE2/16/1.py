h = {}
def f(n):
   if n in h:
        return h[n]
   if n==0:
       h[n]=1
       return 1
   elif n>0:
       h[n] =2*f(1-n)+3*f(n-1)+2
       return 2*f(1-n)+3*f(n-1)+2
   elif n<0:
       h[n]=-f(-n)
       return -f(-n)
print(f(50))
