from itertools import permutations
mn = 10 ** 9
c='21424'*33+'2'*33+'3'*4

for s in permutations(c,len(c)):
    s=''.join(s)
    while '11' in s or '22' in s or '13' in s or '23' in s:
        s=s.replace('11','2',1)
        s = s.replace('22', '21424', 1)
        s = s.replace('13', '2', 1)
        s = s.replace('23', '21424', 1)

    if len(s)<=mn:
        mn=len(s)
        print(s)