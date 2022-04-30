import socket
import re

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
        sock.sendto(message, (broadcastAddress, port))
        sock.settimeout(3.0)
        while True:
            data, addr = sock.recvfrom(4096)
            print(data)
            print(addr)

send_command(broadcastAddress, message, port)