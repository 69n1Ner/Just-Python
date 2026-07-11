from ipaddress import ip_network, ip_address

for x in range(0,256):
    for y in range(0, 256):
        net=ip_network(f'217.19.{x}.{y}/255.255.192.0',0)
        ip=ip_address('217.19.128.131')
        if ip in net:
            print(net)