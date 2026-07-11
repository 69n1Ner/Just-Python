from ipaddress import ip_network
# for mask in range(33):
#     net2=ip_network(f'172.16.168.0/{mask}',0)
#     print(net2.netmask)
masks=[0,128,192,224,240,248,252,254,255]
for x in masks:
    k=0
    net=ip_network(f'172.16.168.0/255.255.255.{x}',0)
    for ip in net:
        ip=bin(int(ip))[2:].zfill(32)
        if ip.count('0')%7==0:
            k+=1
    if k==35:
        print(net,net.netmask)