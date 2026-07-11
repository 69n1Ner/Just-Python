f=open('../../files/17.16_14653.txt')
mas=[int(i) for i in f]

for i in range(len(mas)-3):
    if (99<(mas[i] and mas[i+1])<1000) or \
            (99<(mas[i] and mas[i+2])<1000) or \
            (99<(mas[i] and mas[i+3])<1000) or \
            (99<(mas[i+1] and mas[i+2])<1000) or \
            (99<(mas[i+1] and mas[i+3])<1000) or \
            (99<(mas[i+2] and mas[i+3])<1000):
        if (mas[i]%18==0 and mas[i+1]%18 and mas[i+2]%18 and mas[i+3]%18) or \
                (mas[i+1]%18==0 and mas[i]%18 and mas[i+2]%18 and mas[i+3]%18) or \
                (mas[i+2]%18==0 and mas[i+1]%18 and mas[i]%18 and mas[i+3]%18) or \
                (mas[i+3]%18==0 and mas[i+1]%18 and mas[i+2]%18 and mas[i]%18):
            pass