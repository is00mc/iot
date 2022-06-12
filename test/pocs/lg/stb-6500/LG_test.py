import argparse
import socket
import time

'''
FACTORY RESET SEQUENCE

MENU
DOWN X 3
OK
DOWN X 3
1 X 6
0
RIGHT
OK
'''

'''
SETUP SEQUENCE

OK X 5
RIGHT X 2
DOWN
RIGHT
DOWN X 3
OK
169
OK
254
OK
100
OK
5 - HAVE SERVER ADDRESS AS FUNCTION PARAMETER
OK
80
OK
OK
WAIT FOR USER INPUT?
LEFT
OK
'''

cmd = ''

parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store_true', help='send up command')
parser.add_argument('-d', action='store_true', help='send down command')
parser.add_argument('-l', action='store_true', help='send left command')
parser.add_argument('-r', action='store_true', help='send right command')
parser.add_argument('-ok', action='store_true', help='send ok command')
parser.add_argument('-mn', action='store_true', help='send menu command')
parser.add_argument('-num', help='input a number')
parser.add_argument('-dev', help='device ip')
parser.add_argument('-s', help='start sequence - OPTIONS - reset, setup, commercial')

args = parser.parse_args()

dev = args.dev



PORT = 9761
POWER_ON = 'ka 01 01\r'
POWER_OFF = 'ka 01 00\n'
REBOOT = 'ka 01 02\r'
PM_NETWORK_READY = 'sn 01 0c 05\r'
NETAPPLY = 'sn 01 82 80\r'
INPUT_HDMI = 'xb 01 A0\r'
INPUT_DP = 'xb 01 D0\r'
VW2X2 = 'dd 01 22\r'
VWFULL = 'dd 01 44\r'
JUST_SCAN = 'kc 01 09\r' # toggle
NO_SIGNAL_POWER_OFF_OFF = 'fg 01 00\r'
DPM_STANDBY_MODE_OFF = 'fj 01 00\r'
LAN_DAISEY_CHAIN_ON = 'sn 01 84 01\r'
SET_TIME_AUTO = 'fa 01 00 00\r'
SET_DHCP = "sn 01 80 00"
SOFTWARE_VER = 'fz 01 ff\r'
SCAN_INVERSION_ON = 'sn 01 87 01\r'
SCAN_INVERSION_OFF = 'sn 01 87 00\r'
FRAME_CONTROL_ON = 'sn 01 b7 01\r'
FRAME_CONTROL_OFF = 'sn 01 b7 00\r'
UP = 'mc 01 40\r'
DOWN = 'mc 01 41\r'
LEFT = 'mc 01 07\r'
RIGHT = 'mc 01 06\r'
OK = 'mc 01 44\r'
MENU = 'mc 01 43\r'
EXIT = 'mc 01 5B\r'



def numCMD(data):
    num = data + 10
    return f'mc 01 {num}\r'

ZERO = numCMD(0)
ONE = numCMD(1)
TWO = numCMD(2)
THREE = numCMD(3)
FOUR = numCMD(4)
FIVE = numCMD(5)
SIX = numCMD(6)
SEVEN = numCMD(7)
EIGHT = numCMD(8)
NINE = numCMD(9)


resetSequence = [
    # [cmd, number of times to send command, wait time in seconds before next command]
    [MENU, 1, 1], # open menu
    [DOWN, 3, 1], # go down to advanced menu
    [OK, 1, 5], # enter advanced menu and wait 5 seconds for it to popup
    [DOWN, 3, 1], # go down to general
    [ONE, 5, .5], # press 1 5 times quickly
    [ONE, 1, 2], # press 1 a last time and wait for the hidden page to popup
    [ZERO, 1, 2], # press zero for in stop
    [RIGHT, 1, 1], # go right to say yes to confirmation
    [OK, 1, 0] # press ok to confirm in stop
]

initialSetupSequence = [
    # (cmd, wait time in seconds before next command)
    [OK, 5, 1],
    [RIGHT, 2, 1],
    [DOWN, 1, 1],
    [RIGHT, 1, 1],
    [DOWN, 3, 1],
    [OK, 1, 1],
    [ONE, 1, 1],
    [SIX, 1, 1],
    [NINE, 1, 1],
    [OK, 1, 1],
    [TWO, 1, 1],
    [FIVE, 1, 1],
    [FOUR, 1,1 ],
    [OK, 1 , 1],
    [ONE, 1, 1],
    [ZERO, 2, 1],
    [OK, 1, 1],
    [FIVE, 1, 1],
    [OK, 1, 1],
    [EIGHT, 1, 1],
    [ZERO, 1, 1],
    [OK, 1, 1],
    [OK, 2 , 5],
    [LEFT, 1, 1],
    [OK, 1, 1]
]

commercialMenuSequence = [
    #[MENU, 13, .3],
    [ONE, 2, .5],
    [ZERO, 1, .5],
    [FIVE, 1, .5],
    [EXIT, 1, 0]
]



#------------Commands--------------------------------------

def send_command(dev, command, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'[*] connecting to {dev} on {port}')
        s.connect((dev, port))
        print(f'[*] sending command: {command}')
        s.sendall(command.encode())
        data = s.recv(1024)

        print('[*] Received', repr(data))
        return data.decode()


def commandSequence(dev, sequence, port=PORT):
    for items in sequence:
        cmd = items[0]
        repeatTimes = items[1]
        waitTime = items[2]
        count = 1
        while count <= repeatTimes:
            #print(items[0])
            print(count)
            send_command(dev, cmd, port)
            time.sleep(waitTime)
            count += 1

if args.u:
    cmd = UP
elif args.d:
    cmd = DOWN
elif args.l:
    cmd = LEFT
elif args.r:
    cmd = RIGHT
elif args.ok:
    cmd = OK
elif args.mn:
    cmd = MENU
elif args.num:
    cmd = numCMD(args.num)

if cmd:
    send_command(dev, cmd, PORT)

if args.s:
    if args.s == 'reset':
        commandSequence(args.dev, resetSequence)
    elif args.s == 'setup':
        commandSequence(args.dev, initialSetupSequence)
    elif args.s == 'commercial':
        commandSequence(args.dev, commercialMenuSequence)
    else:
        print('unknown sequence')
