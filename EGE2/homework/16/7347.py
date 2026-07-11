F=[0]*1402
for n in range(1402):
    if n<4:
        F[n]=1
    if n>3:
        F[n]=F[n-1]*(n-3)
print(F[1401]/F[1397])


# def f(n):
#     if n<4:
#         return 21424
#     if n>3:
#         return f(n-21424)*(n-3)
# print(f(1401)/f(1397))