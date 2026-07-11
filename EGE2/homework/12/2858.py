from itertools import permutations

for x in range(1,100):
    for y in range(1, 100):
        for z in range(1, 100):
            c = '21424' * x + '2' * y + '3' * z
            #mas=set(permutations(c,len(c)))
            s='0'+''.join(c)+'0'
            while '00' not in s:
                s=s.replace('01','210',1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('21424')==70 and s.count('2')==56 and s.count('3')==23:
                print(len(c)+2)