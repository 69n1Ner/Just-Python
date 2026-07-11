from itertools import permutations
s='75'*15+'5'*999+'4'*20
while '74' in s or '75' in s:
    if '75' in s:
        s=s.replace('75','744',1)
    else:
        s=s.replace('74','44',1)
print(s.count('4'))