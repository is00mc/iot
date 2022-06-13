import argparse
import socket
import time

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
parser.add_argument('-s', help='start sequence - OPTIONS - reset, setup1, setup2, commercial')
parser.add_argument('-off', action='store_true', help='power off')
parser.add_argument('--server', help='media server address')
parser.add_argument('-a', action='store_true', help='set ascpect ration to 16:9')
parser.add_argument('-i', help='input file for list of devices to configure')


args = parser.parse_args()
devs = []

if args.dev:
    devs.append(args.dev)
if args.i:
    with open(args.i, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            line = line.strip()
            if not line.startswith('#') and line:
                devs.append(line)

PORT = 9761
POWER_ON = 'ka 01 01\r'
POWER_OFF = 'ka 01 00\r'
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
ASPECT = 'kc 01 02\r'



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
    [ONE, 5, .1], # press 1 5 times quickly
    [ONE, 1, 2], # press 1 a last time and wait for the hidden page to popup
    [ZERO, 1, 2], # press zero for in stop
    [RIGHT, 1, 1], # go right to say yes to confirmation
    [OK, 1, 0] # press ok to confirm in stop
]

initialSetupSequence1 = [
    # (cmd, wait time in seconds before next command)
    [OK, 5, 1],
    [OK, 1, 3],
    [OK, 1, .1],

]


initialSetupSequence2 = [
    # (cmd, wait time in seconds before next command)
    [DOWN, 4, 1],
    [OK, 1, 1],
    # insert addrToIR
    #[OK, 1 , 1],
    [OK, 1, 1],
    [EIGHT, 1, 1],
    [ZERO, 1, 1],
    [OK, 1, 1],
    [OK, 2 , 10],
    [LEFT, 1, 1],
    [OK, 1, 1]
]


def addrToIR(addr):
    IR = []
    insert = 2
    for ch in addr:
        if ch == '.':
            IR.append([OK, 1, 1])
        else:
            IR.append([numCMD(int(ch)), 1, 1])
    for i in IR:
        initialSetupSequence2.insert(insert, i)
        insert += 1
    return IR


commercialMenuSequence = [
    [MENU, 11, .1],
    [NINE, 1, .5],
    [EIGHT, 1, .5],
    [SEVEN, 1, .5],
    [SIX, 1, .5],
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


def commandSequence(devs, sequence, port=PORT):
    for items in sequence:
        cmd = items[0]
        repeatTimes = items[1]
        waitTime = items[2]/len(devs)
        count = 1
        while count <= repeatTimes:
            for dev in devs:
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
elif args.a:
    cmd = ASPECT
elif args.off:
    cmd = POWER_OFF

if cmd:
    for d in devs:
        send_command(d, cmd, PORT)

if args.s:
    if args.s == 'reset':
        commandSequence(devs, resetSequence)
    elif args.s == 'setup1':
        commandSequence(devs, initialSetupSequence1)
        print('manually set Pro:Centric Mode to html')
        print('and Media Type to IP')
        print('put cursor on Pro:Centric Mode (html)')
        print('then continue with setup sequence 2 ( -s setup2 --server <server address>)')
    elif args.s == 'setup2':
        addrToIR(args.server)
        commandSequence(devs, initialSetupSequence2)
    elif args.s == 'commercial':
        commandSequence(devs, commercialMenuSequence)
    else:
        print('unknown sequence')
