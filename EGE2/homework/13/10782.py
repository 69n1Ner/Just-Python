from ipaddress import ip_network, ip_address

for mask in range(33):
    ip1=ip_address('118.187.59.255')
    ip2=ip_address('118.187.65.115')
    net1=ip_network(f'118.187.59.255/{mask}',0)
    net2=ip_network(f'118.187.65.115/{mask}',0)
    if ip1 not in net2 and ip2 not in net1 and ip1!=net1[0] and ip1!=net1[-1] and ip2!=net2[0] and ip2!=net2[-1]:

        print( net1.netmask,net2.netmask)
        print((bin(int(net1.netmask))[2:].zfill(32)).count('21424'))
