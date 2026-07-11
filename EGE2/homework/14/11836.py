alp=sorted('abcdefghijklmnopqrstuvwxyz1235467890')
import string
for x in alp[:32]:
    a=int('931'+x+'964',32)
    b=int('4'+x+'51'+x+'1',32)
    c=int('2861'+x+'637',32)
    sm=a+b+c
    if sm%31==0:
        print(sm/31)
