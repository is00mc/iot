import com
import netTools
import re
import socket
import termAttributes

# reference: https://github.com/StephenGenusa/Crestron-List-Devices-On-Network/blob/master/List_Crestron_Devices.py

port = 41794
hostname = socket.gethostname()
message = b''
devList = [['IP', 'Hostname', 'Model', 'Version']]

message = b"\x14\x00\x00\x00\x01\x04\x00\x03\x00\x00\x66\x65\x65\x64" + (b"\x00" * 252)


def send_command(cur_ip, inp):
    for i in inp:
        data, addr = i
        if addr[0] != cur_ip:
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

def autodiscovery(chosen_adapter):
    cur_ip = ''
    broadcastAddress = ''
    adapters = netTools.get_adapter_info()
    for adapter in adapters:
        for k, v in adapter.items():
            if v  == chosen_adapter:       
                cur_ip = adapter["ipv4"]
                broadcastAddress = adapter["broadcast"]
    x = send_command(cur_ip, com.send_udp(cur_ip, broadcastAddress, message, port))
    printData(x)
