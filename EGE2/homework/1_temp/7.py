def f(x,y):
    if x < y or x == 24:
        return 0
    elif x == y:
        return 1
    else:
        if x > 9:
            return f(x-1,y)+f(int(x**0.5),y)+f(x//10,y)
        else:
            return f(x - 1, y) + f(int(x ** 0.5), y)
print(f(602,7))