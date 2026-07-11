from ipaddress import ip_network
k=0
net=ip_network('192.168.32.48/255.255.255.240',0)
for i in net:
    ip=bin(int(i))
    if ip.count('1')%2!=0:
        k+=1
print(k)