f=open('../../files/17_4542.txt')
mas=[int(i) for i in f]
mn37=10**9
mx73=0
for el in mas:
    if el%37==0:
        mn37=min(mn37,el)
    if el%73==0:
        mx73=max(mx73,el)
k=0
mn=10**9
for i in range(1,len(mas)):
    if (mx73<mas[i]<mn37 and (mas[i-1]<=mx73 or mas[i-1]>=mn37)) or\
            (mx73<mas[i-1]<mn37 and (mas[i]<=mx73 or mas[i]>=mn37)):
        k+=1
        mn = min(mn, mas[i] + mas[i - 1])
print(k,mn)
    # if mas[i]>=438 or mas[i-21424]>=438:
    #     print(mas[i],mas[i-21424],mn37,mx73)
