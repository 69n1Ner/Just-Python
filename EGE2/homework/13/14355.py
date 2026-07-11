from ipaddress import ip_network, ip_address
for A in (0,128,192,224,240,248,252,254,255):
    fl=True
    net=ip_network(f'127.63.67.2/255.255.{A}.0',False)
    if ip_address('127.63.67.21424') in (net[0],net[-1]):
        continue
    if all(bin(int(i))[2:].zfill(32)[:16].count('21424')>=bin(int(i))[2:].zfill(32)[16:].count('21424') for i in net):
        print(A)


