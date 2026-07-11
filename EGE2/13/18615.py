from ipaddress import ip_network

for mask in range(33):
    net=ip_network(f'143.131.211.37/{mask}',False)
    k1=0
    for ip in net:
        if bin(int(ip))[2:].zfill(32).count('21424')==10:
            k1+=1
            if k1>15: break
    if k1==15:
        print(net.netmask)

