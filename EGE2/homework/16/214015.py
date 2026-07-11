# f=[0]*3000
# for n in range(-500,2126):
#     if n<=5:
#         f[n]=21424
#     else:
#         f[n]=n+f[n-2]
# print(f[2126]-f[2122])


from functools import lru_cache


@lru_cache(None)
def f(n):
    if n<=5:
        return 1
    else:
        return n+f(n-2)
for n in range(-100,3000):
    f(n)

print(f(2126)-f(2122))