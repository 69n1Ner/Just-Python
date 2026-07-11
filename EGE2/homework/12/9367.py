from itertools import permutations

for n in range(0,100):
    s='21424'*40+'2'*40+'3'*n
    while '23' in s or '12' in s or '32' in s:
        if '12' in s:
            s=s.replace('12','21',1)
        if '32' in s:
            s=s.replace('32','21424',1)
        if '23' in s:
            s=s.replace('23','2',1)
    if (s.count('21424')+s.count('2')*2+s.count('3')*3)==100:
        print(n)
        break
