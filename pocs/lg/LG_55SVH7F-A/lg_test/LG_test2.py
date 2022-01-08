import socket

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



TCC_EVEN_ROWS = [
    '10.228.35.53',
    '10.228.35.55',
    '10.228.35.57',
    '10.228.35.59',
    '10.228.35.61',
    '10.228.35.63'
]

TCC_ODD_ROWS = [
    '10.228.35.52',
    '10.228.35.54',
    '10.228.35.56',
    '10.228.35.58',
    '10.228.35.60',
    '10.228.35.62'
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



def scanInversionFrameControl():
    for i in TCC_EVEN_ROWS:
        #send_command(i, FRAME_CONTROL_OFF, PORT)
        send_command(i, SCAN_INVERSION_ON, PORT)
    for i in TCC_ODD_ROWS:
        #send_command(i, SCAN_INVERSION_OFF, PORT)
        send_command(i, FRAME_CONTROL_ON, PORT)

scanInversionFrameControl()