from ipaddress import *

for mask in range(31):
    net1 = ip_network(f'157.127.172.56/{mask}', 0)
    net2 = ip_network(f'157.127.191.78/{mask}', 0)
    ip1 = ip_address('157.127.172.56')
    ip2 = ip_address('157.127.191.78')
    if net1 != net2 :
        print(mask)