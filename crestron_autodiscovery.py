import socket
import re

# reference: https://github.com/StephenGenusa/Crestron-List-Devices-On-Network/blob/master/List_Crestron_Devices.py

cur_ip = "192.168.25.234"
port = 41794
hostname = socket.gethostname()
message = b''
broadcastAddress = '192.168.25.255'

message = b"\x14\x00\x00\x00\x01\x04\x00\x03\x00\x00\x66\x65\x65\x64" + (b"\x00" * 252)


def send_command(dev, command, port):

    #encode command into bytes
    bytesToSend = command

    # Create a UDP socket at client side
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((cur_ip, port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(message, (dev, port))
        sock.settimeout(3.0)
        devList = []
        while True:
            try:
                data, addr = sock.recvfrom(4096)
                if addr[0] != cur_ip:
                    devList.append(parse_input(data, addr))
            except socket.timeout:
                return devList

def parse_input(data, addr):
    ipAddress = addr[0]
    hostname = re.findall(b'\x00([a-zA-Z0-9-]{2,30})\x00', data)
    ver = re.findall(b'v\d+.\d+.\d+', data)
    dev = re.findall(b'\x00([a-zA-Z0-9-]{2,30}) \[', data)
    for i in ver:
        ver = i.decode()
    for i in dev:
        dev = i.decode()
    retval = [ipAddress, hostname[0].decode(), dev, ver]
    return retval

def printData(data):
    x = 14
    print("{:<14} {:<15} {:<7} {:<5}".format('IP','Hostname','Model', 'Version'))
    print('--------------------------------------------------')
    for d in data:
        IP,Hostname, Model, Version = d
        print ("{:<14} {:<15} {:<7} {:<1}".format(IP,Hostname,Model, Version))
        # print(f"Model: {d[3]}, hostname: {d[1]}, ip address: {d[0]}, version: {d[2]}")

printData(send_command(broadcastAddress, message, port))


'''
text = b'\x15\x00TSW-55-7F48DE26\x00'
test = re.findall(b'\x00([a-zA-Z0-9-]{2,30})\x00', text)
print(test)
'''