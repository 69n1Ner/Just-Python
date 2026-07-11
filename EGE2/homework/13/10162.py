from ipaddress import *
for mask in range(33):
    net1=ip_network(f'112.117.107.70/{mask}',0)
    net2=ip_network(f'112.117.121.80/{mask}',0)
    ip1=ip_address('112.117.107.70')
    ip2=ip_address('112.117.121.80')
    if net1==net2 and net1[0]<ip1<net1[-1] and net2[0]<ip2<net2[-1]:
        print(net1,net1.netmask)
