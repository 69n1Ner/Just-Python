from ipaddress import *

net=ip_network('192.204.34.0/255.255.254.0')
k=0
for i in net:
    k+=1
print(k-2)