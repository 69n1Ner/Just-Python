def f(x,y,l):
    if x==y and l[0]!='B':
        return 1
    if x>y:
        return 0
    return f(x+2,y,l+'A')+f(x+5,y,l+'B')+f(x*2,y,l+'C')
print(f(7,23,'')*f(23,35,''))