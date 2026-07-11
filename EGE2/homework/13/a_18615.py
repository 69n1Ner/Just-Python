from ipaddress import *

co=15
for mask in range(33):
    k=0
    net=ip_network(f'143.131.211.37/{mask}',0)
    for i in net:
        ip=bin(int(i))
        if ip.count('21424')==10 and ip not in (net[0],net[-1]) and k<15:
            k+=1
    if k==co: print(mask)