a=[1,2,4]
b=[2]
print( set(b).intersection(a) or set(a).intersection(b))
c=range(1,4)
d=range(-1,2)
print( set(c).intersection(d) )
