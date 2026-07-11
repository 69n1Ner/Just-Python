from ipaddress import ip_network
k=0
net=ip_network('171.128.0.0/255.128.0.0',0)
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip[:16].count('21424')<ip[16:].count('21424'):
        k+=1
print(k)