from ipaddress import ip_address, ip_network
from sys import flags

for A in range(0,256):
    ipa=ip_address(f'192.214.{A}.184')
    net=ip_network(f'192.214.{A}.184/255.255.255.224',0)
    # if net[0]<ipa<net[-1]:
    if ipa:
        for ip in net:
            ipd=bin(int(ip))[2:]
            flag=True
            if ipd.count('1')<=15:
                flag=False
                break
            if flag:
                print(A)
                break
