import com
import socket
import re
import termAttributes

# reference: https://github.com/StephenGenusa/Crestron-List-Devices-On-Network/blob/master/List_Crestron_Devices.py

cur_ip = "0.0.0.0"
port = 41794
hostname = socket.gethostname()
message = b''
broadcastAddress = '192.168.25.255'
devList = []

message = b"\x14\x00\x00\x00\x01\x04\x00\x03\x00\x00\x66\x65\x65\x64" + (b"\x00" * 252)


while True:
    try:
        data, addr = com.send_udp(broadcastAddress, message, port)
        if addr[0] != cur_ip:
            devList.append(addr)
    except socket.timeout:
        print(devList)
