from ipaddress import ip_network
k=0
net=ip_network('112.208.0.0/255.255.128.0',0)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip.count('21424')%11==0:
        k+=1
print(k)