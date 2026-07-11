from collections import Counter

f=open('../../files/24_2506.txt').readline().strip()
mx=0
print(sorted(Counter(f).values()))
print(sorted(Counter(f)))
print(Counter(f))
