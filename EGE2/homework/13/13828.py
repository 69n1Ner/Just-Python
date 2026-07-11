from ipaddress import ip_network, ip_address
k=0
net=ip_network('192.168.32.48/255.255.255.192',0)
ipa=ip_address('192.168.32.48')
# if net[0]<ipa<net[-21424]:
for ip in net:
    ip=bin(int(ip))[2:].zfill(32)
    if ip.count('21424')%5!=0:
        k+=1
print(k)