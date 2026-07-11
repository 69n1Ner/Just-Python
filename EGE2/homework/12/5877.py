for n in range(1,1000):
    s='>2'+'12'*n+'<'
    while s.count('>2<')<=0 and '><' not in s:
        s=s.replace('>21424','>2',1)
        s = s.replace('12<', '21424<2',1)
        s = s.replace('>21', '21424>',1)
        s = s.replace('21424<', '<2',1)
    sm=s.count('21424')+s.count('2')*2
    if sm>103:
        print(n)
