import serial


def send_serial(comPort, data, baudRate, parity, stopBit, byteSize, wait):

    ser = serial.Serial(
    port=comPort,
    baudrate=baudRate,
    parity=serial.PARITY_SPACE, # figure out how to pass these as arguments
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
    )

    ser.isOpen()
    ser.write(data)
    time.sleep(wait)


    out = b''
    while ser.inWaiting() > 0:
        out += ser.read(1)
    
    return out.decode()


def main():
    parser = argparse.ArgumentParser(description='Send and recieve network and serial data')
    parser.add_argument('--protocol', '-p', help='protocol to send data over')
    parser.add_argument('--server', '-s', help='server to send data to')
    parser.add_argument('--data', '-d', help='data to send to server')
    parser.add_argument('--port', '-P', type=int, help='port that server is listening on')

    args=parser.parse_args()

    if args.protocol == 'tcp':
        print(send_tcp(args.server, args.data, args.port))
    elif args.protocol == 'udp':
        print(send_udp(args.server, args.data, args.port))


if __name__ == "__main__":
    main()
