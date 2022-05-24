import socket
import sys

f = sys.argv[1]

nh = []
hosts = {}

with open(f, 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        dev = line.strip()
        try:
            print(f'getting hostname for {dev}')
            x = socket.gethostbyaddr(dev)
            print(x[0])
            hosts[dev] = x[0]
        except socket.herror:
            print('no hostname')
            nh.append(dev)
print()
print('--------------------')
print('addresses with hostnames:')
for k,v in hosts.items():
    print(k, v)

print()
print('--------------------')
print('no hostname for the following addresses')
for i in nh:
    print(i)
