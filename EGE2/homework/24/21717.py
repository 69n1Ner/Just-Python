f=open('../../files/24_21717.txt').readline()
mn=10000
for l in range(len(f)):
    for r in range(l+mn,l,-1):
        stro=f[l:r+1]
        if stro.count('RSQ')<130:
            break
        elif stro.count('RSQ')==130 and stro[-1]!='Q':
            mn=min(mn,len(stro))
print(mn)