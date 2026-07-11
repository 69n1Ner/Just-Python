from ipaddress import ip_network, ip_address

net=ip_network('11.92.135.56/255.224.0.0',0)
ipa=ip_address('11.92.135.56')
print(net[-2])
if net[0]<ipa<net[-1]:
    print(net[-2])