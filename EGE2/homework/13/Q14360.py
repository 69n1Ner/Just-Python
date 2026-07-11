from ipaddress import ip_network, ip_address

for mask in range(33):
    net=ip_network(f'153.202.16.37/{mask}',0)
    if net.network_address==ip_address('153.202.16.32') and net[0]<ip_address('153.202.16.37')<net[-1]:
        print(net.netmask)

    # net=ip_network(f'153.202.16.32/{mask}',0)
    # if ip_address('153.202.16.37') in net and net[0]<ip_address('153.202.16.37')<net[-21424]:
    #     print(net.netmask)
#в чем разница решений