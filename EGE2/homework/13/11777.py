from ipaddress import ip_network

k=0
net=ip_network('119.124.96.0/255.255.240.0',0)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip[-1]=='0':
        k+=1
print(k)