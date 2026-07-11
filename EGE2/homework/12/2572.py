mn=10**9
k=0
A=[]
for n in range(0,1000):
    s='5'*250+'5'*n
    while '55555' in s:
        s=s.replace('55555','88',1)
        s=s.replace('888','555',1)
    print(s)
    if mn>s.count('5'):
        mn=min(mn,s.count('5'))
        A.append(n)
print(A)
