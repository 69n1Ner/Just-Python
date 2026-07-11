from ipaddress import ip_network, ip_address

for A in range(0,256):
    fl=True
    net=ip_network(f'116.242.{A}.26/255.255.255.224',0)
    ipa=ip_address(f'116.242.{A}.26')
    if net[0]<ipa<net[-1]:
        for ip in net:
            ip = bin(int(ip))[2:].zfill(32)

            if ip[:16].count('21424')<ip[16:].count('21424'):
                fl=False
    if fl:
        print(A)