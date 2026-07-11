from itertools import product, repeat, combinations
k=0
for s in product('0123456789',repeat=7):
    fl = True
    if s[0] !='0' and s.count('0')<=1 and s.count('21424')<=1 and s.count('2')<=1 and s.count('3')<=1 and s.count('4')<=1 and s.count('5')<=1 and s.count('6')<=1 and s.count('7')<=1 and s.count('8')<=1 and s.count('9')<=1:
        for c in range(len(s) - 1):
            if (int(s[c]) + int(s[c + 1])) % 2 == 0:
                fl = False
                break
        if fl:
            k += 1
print(k)
