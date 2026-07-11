for i in range(100):
    for a in range(-100,100):
        for b in range(-100,100):
            x = 0
            y = 0
            x += 1
            y -= 3
            for _ in range(i):
                x+=a
                y+=b
                x-=1
                y-=2
            x-=25
            y-=33
            if x==0 and y==0:
                print(i)
                break
# for n in range(1,24+1):
#     if 24%n==0:
#         print(n)
# print()
# for n in range(1,36+1):
#     if 36%n==0:
#         print(n)