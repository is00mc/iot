import time
import serial
import sys

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

# get keyboard input
i = sys.argv[1].encode()
# send the character to the device
# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
ser.write(i + b'\n')
out = b''
# let's wait one second before reading output (let's give device time to answer)
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)
    
if out != '':
    print(out)
