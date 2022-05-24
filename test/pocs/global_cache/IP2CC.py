import socket
import time

PORT = 4998
RELAY1ON = 'setstate,1:1,1\r'
RELAY1OFF = 'setstate,1:1,0\r'
RELAY2ON = 'setstate,1:2,1\r'
RELAY2OFF = 'setstate,1:2,0\r'
RELAY3ON = 'setstate,1:3,1\r'
RELAY3OFF = 'setstate,1:3,0\r'

def send_command(dev, command, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'[*] connecting to {dev} on {port}')
        s.connect((dev, port))
        print(f'[*] sending command: {command}')
        s.sendall(command.encode())
        data = s.recv(1024)

        print('[*] Received', repr(data))

send_command('192.168.1.70', RELAY1ON, PORT)
send_command('192.168.1.70', RELAY2ON, PORT)
send_command('192.168.1.70', RELAY3ON, PORT)
time.sleep(2)
send_command('192.168.1.70', RELAY1OFF, PORT)
send_command('192.168.1.70', RELAY2OFF, PORT)
send_command('192.168.1.70', RELAY3OFF, PORT)
