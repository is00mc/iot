import argparse
import socket
import time


def send_tcp(server, data, port, buffer=1024, timeout=3.0):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((server, port))
        s.sendall(data.encode())
        s.settimeout(timeout)
        response = s.recv(buffer)

    return response


def send_udp(bind_addr, server, data, port, buffer=1024, timeout=3.0):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        responses = []
        s.bind((bind_addr, port))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(data, (server, port))
        try:
            while True:
                s.settimeout(3.0)
                responses.append(s.recvfrom(buffer))
        except socket.timeout:
            return responses

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--protocol')
    parser.add_argument('-s', '--server')
    parser.add_argument('-P', '--port')
    parser.add_argument('-d', '--data')

    args = parser.parse_args()

    if args.protocol == 'tcp':
        send_tcp(args.server, args.data, args.port)


if __name__ == "__main__":
    main()
