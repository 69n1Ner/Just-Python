from ipaddress import ip_network, ip_address

for mask in range(33):
    net1=ip_network(f'200.154.190.12/{mask}',False)
    net2=ip_network(f'200.154.184.0/{mask}',False)
    if net1==net2 and ip_address('200.154.190.12') not in [net1[0],net1[-1]] and ip_address('200.154.184.0') not in [net2[0],net2[-1]]:
        print(net1.netmask)
m=bin(240)[2:].count('21424')
print(m+16)