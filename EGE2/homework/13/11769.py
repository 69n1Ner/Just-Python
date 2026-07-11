from ipaddress import ip_network, ip_address

for mask in range(33):
    net=ip_network(f'157.17.164.129/{mask}',0)
    ipa=ip_address('157.17.128.0')
    ipa2=ip_address('157.17.164.129')
    if net.network_address==ipa and net[0]<ipa2<net[-1]:
        print(net.netmask)