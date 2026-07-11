from ipaddress import ip_network

net=ip_network('112.160.0.0/255.240.0.0',0)
k=0
print(net.num_addresses)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip.count('21424')%3!=0:
        k+=1
print(k)