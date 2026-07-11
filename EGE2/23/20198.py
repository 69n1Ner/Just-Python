def f(x,y,p):
    if x==y and 'aaa' not in p:
        return 1
    if x>y+3 or x<0 or 'aaa' in p:
        return 0
    return f(x-1,y,p+'a') + f(x+5,y,p+'b') +f(x*2,y,p+'c')
print(f(5,34,''))
