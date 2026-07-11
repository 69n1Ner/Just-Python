from ipaddress import ip_network, ip_address

net=ip_network('143.168.72.213/255.255.255.240',0)
ip_ad=ip_address('143.168.72.213')
mx=0
if ip_ad in net:
    for ip in net:
        if ip!=net[0] and ip!=net[-1]:
            mx=max(mx,int(ip))
            print(ip)
print(mx)