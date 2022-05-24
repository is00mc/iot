import argparse
import time
import serial

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--comport', help='computers com port')

args  = parser.parse_args()
ip = ''
sm = ''
gw = ''

esc = bytes.fromhex('1b').decode()
get_ip =f"{esc}ci\r"
set_ip = f"{esc}{ip}ci\r"
get_subnet = f"{esc}cs\r"
set_subnet = f"{esc}{sm}cs\r"
get_gateway = f"{esc}cg\r"
set_gateway = f"{esc}{gw}cg\r"
check_dhcp = f"{esc}dh\r"
dhcp_on = f"{esc}1dh\r"
dhcp_off = f"{esc}0dh\r"
get_fw = f"Q"
get_fw_and_build = "*Q"



# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port=args.comport,
    baudrate=9600,
    parity=serial.PARITY_SPACE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

#print('Enter your commands below.\r\nInsert "exit" to leave the application.')

Input=1

def get_IP():
    x = 0
    while x == 0 :
        # get keyboard input
        #input = raw_input(">> ")
            # Python 3 users
        #Input = input(">> ")
        print('getting ip address')
        Input = f"{esc}ci\r"
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(Input.encode())
        out = b''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)
            
        if out != b'':
            ip = out.decode().strip()
            print(f'ip: {ip}')
            if ip.strip() == '0.0.0.0':
                print('error try again')
                ser.close()
                exit()
            else:
                return ip

def send_command(command):
    ser.write(command.encode())
    out = b''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)
    print(out.decode().strip())
    return

#ip = get_IP()
#print('checking dhcp')
#send_command(check_dhcp)
#print('disabling dhcp')
#send_command(dhcp_off)
#print(f'setting ip to {ip}')
#send_command(set_ip)
print('getting fw')
send_command(get_fw)
print('getting fw and build')
send_command(get_fw_and_build)
ser.close()
exit()
