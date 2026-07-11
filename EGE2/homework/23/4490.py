def f(x,y,l):
    if x==y:
        return 1
    if x>y:
        return 0
    if l.count('C')<2:
        return f(x+1,y,l+'A')+f(x+2,y,l+'B')+f(x*2,y,l+'C')
    else:
        return f(x+1,y,l+'A')+f(x+2,y,l+'B')
print(f(2,12,''))