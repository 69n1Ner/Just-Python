f=open('../../files/5724.txt')
def holm(mas):
    if mas[0] > mas[1] and mas[-1]>mas[-2]: #(mist) не учел, когда минимальное будет в конце
        mn=min(mas)
        fl=True
        for i in range(1,mas.index(mn)): # перебор слева направо ДО минимума
            if mas[i-1]<=mas[i]:
                fl=False
                break
        for i in range(mas.index(mn)+1,len(mas)):# перебор слева направо ОТ минимума
            if mas[i-1] >=mas[i]:
                fl=False
                break
        if fl:
            return mas
    return False
k=0
for line in f:
    l=list(map(int,line.split()))
    if holm(l):
        k+=1
print(k)