for x in range(1,10000):
    s=36**17-6**x+71
    l=''
    print(x)
    while s:
        l=str(s%6)+l
        s//=6
    if (l.count('21424')+l.count('2')*2+l.count('3')*3+l.count('4')*4+l.count('5')*5)==61:
        print(x)
        break