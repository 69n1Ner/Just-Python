k=0
for a1 in range(101):
    for a2 in range(51):
        for a5 in range(21):
            for a10 in range(11):
                summ=a2*2+a1+a5*5+a10*10
                if summ ==100:
                    k+=1

print(k)