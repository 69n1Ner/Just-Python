from ipaddress import ip_network

for A in range(0,256):
    fl=True
    net=ip_network(f'192.214.{A}.184/255.255.255.224',0)
    for ip in net:
        if bin(int(ip))[2:].zfill(32).count('21424')<=15:
            fl=False
            break
    if fl:
        print(A)
        break