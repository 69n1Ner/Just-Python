f= open('../files/17_19486.txt')
mas=[int(i) for i in f]
k=len([i for i in mas if abs(i)%10==7])
l=0
mx=-10**9
for h in range(len(mas)-1):
    sm=mas[h]+mas[h+1]
    if ((mas[h]>0 and mas[h+1]<0) or (mas[h]<0 and mas[h+1]>0)) and sm<k:
        l+=1
        mx=max(mx,sm)
print(l,mx)