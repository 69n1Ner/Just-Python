s='21424'+'0'*105
while '21424' in s:
    if '100' in s:
        s=s.replace('100','0001',1)
    else:
        s=s.replace('21424','00',1)
print(s.count('0'))
