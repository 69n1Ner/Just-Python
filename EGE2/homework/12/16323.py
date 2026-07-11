x='8'*82
while '1111' in x or '8888' in x:
    if '1111' in x:
        x=x.replace('1111','8',1)
    else:
        x=x.replace('8888','11',1)
print(x)