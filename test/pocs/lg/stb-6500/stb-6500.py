import argparse
import time
import serial
from serial.serialutil import XON

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--comport', help='computers com port')

args  = parser.parse_args()
ip = ''
sm = ''
gw = ''

POWER_ON = 'ka 01 01\r'
POWER_OFF = 'ka 01 00\n'


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port=args.comport,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    xonxoff = True
)


#print('Enter your commands below.\r\nInsert "exit" to leave the application.')

Input=1

def send_command(command):
    ser.isOpen()
    print(f'sending {command}')
    ser.write(command.encode())
    out = b''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)
        print(f'recieving {out}')
    return out.decode().strip()

send_command(POWER_OFF)
ser.close()
exit()
