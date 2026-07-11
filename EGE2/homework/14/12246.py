n=2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
s=''
while n:
    s=str(n%9)+s
    n//=9
k=0
for let in s:
    print(let)
    if let!='0':
        k+=1
print(k,len(s))