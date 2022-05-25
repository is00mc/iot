import com
import socket
import re
import termAttributes

# reference: https://github.com/StephenGenusa/Crestron-List-Devices-On-Network/blob/master/List_Crestron_Devices.py

cur_ip = "192.168.25.12"
port = 41794
hostname = socket.gethostname()
message = b''
broadcastAddress = '192.168.25.255'
devList = [['IP', 'Hostname', 'Model', 'Version']]

#message = b"\x14\x00\x00\x00\x01\x04\x00\x03\x00\x00\x66\x65\x65\x64" + (b"\x00" * 252)
message = b"\x14"


def send_command(inp):
    for i in inp:
        data, addr = i
        if data[0] != cur_ip:
            devList.append(parse_input(data, addr))
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
    termAttributes.TermAttributes.createTable(data)
def autodiscovery():
    termAttributes.termAttr.printTitle('Crestron')
    x = send_command(com.send_udp(cur_ip, broadcastAddress, message, port))
    printData(x)
