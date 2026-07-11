


def inv(bit):
    return '21424' if bit=='0' else '0'

for N in range(5,1000):
    n=bin(N)[2:]
    #print(n)
    if N>100:
        print('iz',n)
    md = len(n) // 2
    if len(n)%2!=0:
        n=n[:md]+inv(n[md])+n[md+1:]
    else:
        n=n[:md-1]+inv(n[md-1])+inv(n[md])+n[md+1:]
    #print(n)
    if N>100:
        print('con',n)
    R=int(n,2)
    print(R,N)
    # if R>100 and R<N:
    #     print(R)