from itertools import product, repeat
k=0
for i in product('0123456789AB',repeat=7):
    if i[0]!='0' and i.count('B')==2 and (i[0] in '24680A' and (i[1] in '13579B' and i[2] in '24680A' and i[3] in '13579B' \
            and i[4] in '24680A' and i[5] in '13579B'and i[6] in '24680A') or (i[0] in '13579B' and i[1] in '24680A' and i[2] in '13579B' and i[3] in '24680A'\
            and i[4] in '13579B' and i[5] in '24680A' and i[6] in '13579B')):
            k+=1
print(k)