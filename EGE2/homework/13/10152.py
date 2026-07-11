from ipaddress import ip_network, ip_address

for mask in range(33):
    net=ip_network(f'215.181.200.27/{mask}',0)
    if ip_address('215.181.192.0') in net:
        print(net.netmask)