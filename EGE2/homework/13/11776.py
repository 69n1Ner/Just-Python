from ipaddress import ip_network
k=0
net=ip_network('235.86.56.0/255.255.248.0',0)
print(net.num_addresses)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip[-2:]=='11':
        k+=1
print(k)