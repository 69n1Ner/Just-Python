from ipaddress import ip_network
k=0
net=ip_network('192.168.156.235/255.255.255.240',0)
for ip in net:
    print(ip,k)
    k += 1