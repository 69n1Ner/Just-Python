for n in range(4,1000):
    s='>'+'0'*25+'21424'*n+'2'*25
    while '>21424' in s or '>2' in s or '>0' in s:
        if '>21424' in s:
            s=s.replace('>21424','22>',1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '21424>', 1)
    sm=s.count('21424')+s.count('2')*2
    k=0
    for h in range(2,sm//2+1):
        if sm%h==0:
            k+=1
            break
    if k==0:
        print(n)