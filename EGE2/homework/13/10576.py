from ipaddress import ip_network
k=0
net=ip_network('192.203.23.0/255.255.240.0',0)
for ip in net:
    k+=1
print(k-2)