from ipaddress import ip_network
k=0
net=ip_network('105.224.200.224/255.255.255.224',0)
for ip in net:
    ip=bin(int(ip))
    if ip.count('1')%4==0:
        k+=1
print(k)