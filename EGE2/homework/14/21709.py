mx=0
for x in range(1,3000):
    w=4**210+4**110-x
    s=''
    while w:
        s=str(w%4)+s
        w//=4
    mx=max(mx,s.count('0'))
    if mx==105:
        print(x)
print(mx)