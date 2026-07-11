def f(x,y,h):
    if x==y and 'CAC' in h:
        return 1
    if x>y:
        return 0
    return f(x+1,y,h+'A')+f(x*3,y,h+'B')+f(x+5,y,h+'C')
print(f(3,69,''))