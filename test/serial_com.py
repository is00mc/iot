import serial
import sys
import time


def send_serial(comPort, data):

    ser = serial.Serial(
    port=comPort,
    baudrate='9600',
    parity=serial.PARITY_SPACE, # figure out how to pass these as arguments
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
    )

    data += '\r\n'

    ser.isOpen()
    ser.write(data.encode())


    out = b''
    while ser.inWaiting() > 0:
        out += ser.readline()
    
    return out.decode()

send_serial(sys.argv[1], sys.argv[2])
