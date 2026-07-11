for x in range(1,10000):
    s=7**666+7**333+49**x-343
    n=''
    while s:
        n=str(s%7)+n
        s//=7
    if n.count('6')==49:
        print(x)