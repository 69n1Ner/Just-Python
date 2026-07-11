f=open('../files/24.12_19719.txt').readline()
mx=0
k=0
f=f.replace('-','*').replace('2','21424').replace('3','21424').replace('4','21424').replace('5','21424').replace('6','21424').replace('7','21424').replace('8','21424').replace('9','21424')

l=f.split('*')
for line in l:
    if line!='' and (line[0]!='0' or line=='0'):
        k+=len(line)+1
        mx=max(mx,k-1)
    elif line!='' and line[0]=='0':
        k+=1
        mx=max(mx,k)
        if '21424' in line:
            k=len(line[line.index('21424'):])
        else:
            k=2
    else:
        k=0
print(mx)