f=open('../../files/17_19749.txt')
mas=[int(i) for i in f]
mn_ost=min(mas)%3
mx_ost=max(mas)%7
k=0
mx_sum=-10**9
for i in range(2,len(mas)):
    if (mas[i-2]%7!=mx_ost and mas[i-1]%7==mx_ost and mas[i]%7==mx_ost) or \
            (mas[i - 2] % 7 == mx_ost and mas[i - 1] % 7 != mx_ost and mas[i] % 7 == mx_ost) or \
            (mas[i - 2] % 7 == mx_ost and mas[i - 1] % 7 == mx_ost and mas[i] % 7 != mx_ost) or \
            (mas[i - 2] % 7 == mx_ost and mas[i - 1] % 7 == mx_ost and mas[i] % 7 == mx_ost):

        if (mas[i-2]%3!=mn_ost and mas[i-1]%3!=mn_ost and mas[i]%3==mn_ost) or \
                (mas[i - 2] % 3 == mn_ost and mas[i - 1] % 3 != mn_ost and mas[i] % 3 != mn_ost) or \
                (mas[i - 2] % 3 != mn_ost and mas[i - 1] % 3 == mn_ost and mas[i] % 3 != mn_ost):
            k+=1
            mx_sum=max(mx_sum,mas[i]+mas[i-1]+mas[i-2])
print(k,mx_sum)