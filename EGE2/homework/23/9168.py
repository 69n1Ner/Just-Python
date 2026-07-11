A=[]
def f(x,co):
    if co==4:
        A.append(x)
        return 1
    if co>4:
        return 0
    return f(x+2,co+1) + f(x*3,co+1)
print(f(1,0),len(set(A)))
