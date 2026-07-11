from ipaddress import ip_network, ip_address

k=0
for A in range(0,256):
    ip=ip_address(f'246.81.65.{A}')
    net=ip_network(f'246.81.65.{A}/255.255.255.224',0)
    if ip not in (net.network_address,net.broadcast_address):
        if all(f'{ip:b}'[16:24].count('0')>f'{ip:b}'[24:].count('0') for ip in net.hosts()):
            k+=1
print(k)
