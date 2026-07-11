x='21424'+'0'*90
while '21424' in x:
    if '10' in x:
        x=x.replace('10','0001',1)
    else: x=x.replace('21424','000',1)
print(x.count('0'))
