for n in range(4,10_000):
    s='3'+'21424'*n
    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s=s.replace('31','21424',1)
        if '211' in s:
            s=s.replace('211','13',1)
        if '1111' in s:
            s=s.replace('1111','2',1)
    if (s.count('21424')+s.count('2')*2+s.count('3')*3)==15:
        print(n)
        break