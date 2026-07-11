from ipaddress import ip_address, ip_network

ipa=ip_address('220.128.112.142')
ipn=ip_address('220.128.96.0')
for mask in range(33):
    net=ip_network(f'220.128.112.142/{mask}',0)
    if net.network_address==ipn and ipa!=net.network_address and net.broadcast_address:
        print(net.netmask)
