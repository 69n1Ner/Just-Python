from ipaddress import ip_address, ip_network
k=0
ipd=ip_address('192.168.0.0')
net=ip_network('192.168.0.0/255.255.192.0',0)
for ip in net:
    ipa=bin(int(ip))[2:].zfill(32)
    if ipa.count('1')>ipa.count('0'):
        k+=1
print(k)