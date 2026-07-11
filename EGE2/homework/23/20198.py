def f(x,y,fl):
    if x==y and "AAA" not in fl:
        return 1
    if x>(y+3) or 'AAA' in fl:
        return 0
    return f(x-1,y,fl+'A') + f(x+5,y,fl+'B') +f(x*2,y,fl+'C')
print(f(5,34,''))
