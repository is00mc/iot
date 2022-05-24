import socket
import sys

# check if user input was given
if len(sys.argv) < 2:
    print('USAGE: python CDT-100.py [command]')
    print('COMMANDS:')
    print('         red - change LED to red')
    print('         green - change LED to green')
    print('         info - get current LED state')
    print('         ver - get firmware version')
    print('         \"custom\" - enter syntax of any other command in api (in place of \"custom\")')
    exit()

# usage: python clock_audio.py red
# turns leds red

# UDP port to send and listen on
PORT = 49494

# get user input
arg = sys.argv[1]

# list of devices to send command to
devs = ["192.168.121.140", "192.168.121.141", "192.168.121.142", "192.168.121.143", "192.168.121.144", "192.168.121.145", "192.168.121.146", "192.168.121.147", "192.168.121.148", "192.168.121.149"]

# set command based on user input
if arg == "red":
    # turn green off and red on
    command = ["STS 0 G=0\r", "STS 0 R=1\r"]
elif arg == "green":
    # turn red off and green on
    command = ["STS 0 G=1\r", "STS 0 R=0\r"]
elif arg == "info":
    # get LED state
    command = ["GTS 1\r"]
elif arg == 'ver':
    # get firmware version
    command = ["version\r"]
else:
    # send any other command input by user
    command = [f'{arg}\r']

bufferSize          = 1024

 
def send_command(dev, command, port):

    #encode command into bytes
    bytesToSend = str.encode(command)

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    

    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend, (dev, port))

    # set time out

    UDPClientSocket.settimeout(3.0)

    # recieve message from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    

    # format message
    msg = "Message from {} {}".format(dev, msgFromServer[0])

    print(msg)

# iterate through list of devices and send command
for d in devs:
    for cmd in command:
        send_command(d, cmd, PORT)
