#!/usr/bin/env python

from netmiko import ConnectHandler

MT = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': '',
}
net_connect = ConnectHandler(**MT)
output = net_connect.send_command('ip address add address=1.1.1.4/24 interface=ether3')
print(output)