f=open('../../files/17_18957.txt')
mas=[int(i) for i in f]
mx=max(mas)/2
k=0
mx2=-10**9
for i in range(len(mas)-2):
    if ('0' in str(mas[i]) and '0' not in str(mas[i+1]) and '0' not in str(mas[i+2]) \
            or '0' not in str(mas[i]) and '0'  in str(mas[i+1]) and '0' not in str(mas[i+2]) \
            or not '0' in str(mas[i]) and '0' not in str(mas[i+1]) and '0' in str(mas[i+2]) \
            or not '0' in str(mas[i]) and '0' not in str(mas[i+1]) and '0' not in str(mas[i+2])) \
            and (mas[i]+mas[i+1]+mas[i+2])<mx:
        k+=1
        mx2=max(mas[i]+mas[i+1]+mas[i+2],mx2)
print(k,mx2)