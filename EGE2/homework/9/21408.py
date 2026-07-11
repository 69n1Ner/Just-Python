from collections import Counter

f=open('../../files/21408.txt')
for l in f:
    line=l.split()
    c=Counter(line)
    if len(c)==3:
        print(c)