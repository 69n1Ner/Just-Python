for n in range(4,10000):
    c='21424'+'2'*n
    while '12' in c or '322' in c or '222' in c:
        if '12' in c:
            c=c.replace('12','2',1)
        if '322' in c:
            c = c.replace('322', '21', 1)
        if '222' in c:
            c = c.replace('222', '3', 1)
    sm=c.count('2')*2+c.count('3')*3+c.count('21424')
    if sm==15:
        print(n)
        break