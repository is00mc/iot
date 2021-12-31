# TODO
# test date command

import csv
import datetime
import os
import socket
import time


CWD = os.getcwd()
HOSTSCSVHEADERS = ["MACAddress", "IPAddress", "HostName", "something"]
PATH_TO_HOSTS = os.path.join(CWD, "..\\python_dhcp_server\\server\\hosts.csv")
PATH_TO_CONFIG = "LG.csv"

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



SUBNET = '255255255000'
GATEWAY = '192168001001'




def formatIP(ip):
    octets = ip.split('.')
    formattedIPList = []
    formattedIP = ''
    for i in octets:
        if int(i) < 10:
            i = '00' + i
        elif int(i) < 100:
            i = '0' + i
        formattedIPList.append(i)
    formattedIP = ''.join(formattedIPList)
    return formattedIP

def getTime():
    return datetime.datetime.now()


def set_time_hms():
    print(getTime().hour)
    exit()
    hr = format(getTime().hour, 'x')
    print(hr)
    mn = format(getTime().minute, 'x')
    print(mn)
    s = format(getTime().second, 'x')
    print(s)
    return f'fx 01 {hr} {mn} {s}\r'


def changIPAddress(ip, subnet, gateway):
    ip = formatIP(ip)
    subnet = formatIP(subnet)
    gateway = formatIP(gateway)
    return(f'sn 01 80 01 {ip} {subnet} {gateway}\r')

def setDNS(dns):
    dns = formatIP(dns)
    return(f'sn 01 81 {dns}\r')

TILE2X2 = {
    '60': '10',
    '61': '20',
    '62': '10',
    '63': '20',
    '64': '30',
    '65': '40',
    '66': '30',
    '67': '40'
    }

TILEFULL = {
    '52': '10',
    '53': '20',
    '54': '30',
    '55': '40',
    '56': '50',
    '57': '60',
    '58': '70',
    '59': '80',
    '60': '90',
    '61': 'A0',
    '62': 'B0',
    '63': 'C0'
    }

INPUT2X2 = ['56', '57', '60', '61', '62', '63']


VIDEOWALL = [
    '10.228.35.52',
    '10.228.35.53',
    '10.228.35.54',
    '10.228.35.55',
    '10.228.35.56',
    '10.228.35.57',
    '10.228.35.58',
    '10.228.35.59',
    '10.228.35.60',
    '10.228.35.61',
    '10.228.35.62',
    '10.228.35.63'
]

TVS = [
    '10.228.37.63',
    '10.228.37.64',
    '10.228.37.65',
    '10.228.37.66',
    '10.228.37.67',
    '10.228.37.68',
    '10.228.37.69',
    '10.228.37.70',
    '10.228.37.71',
    '10.228.37.72',
    '10.228.37.73',
    '10.228.37.74',
    '10.228.37.75'
]


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

#-----csv shit------------------

def csvToDicts(path): # used
    """
    Iterates through a csv file with an arbitrary number of columns and creates a list of dictionaries
    where the key is the column name and the value is the corresponding value for that column in that row.
    The csv file is passed as the PATH parameter.
    returns the list of dictionaries
    """
    headers = [] # initialize a list for the header
    list = [] # initialize a list for the rows in the csv file. Indices are dictionaries with the rows contents
    with open(path, ) as csvfile:
        reader = csv.reader(csvfile)
        row_count = 0
        for row in reader: # iterates through the rows in the csv file
            if row_count == 0: # checks if the current row is the header row
                for i in row:
                    headers.append(i) # appends the list with header names
                row_count += 1
            else:
                dict = {} # initializes a dictionary to hold the contents of the csv row
                column_count = 0
                for i in row: # iterates through the columns of the current row
                    dict[headers[column_count]] = row[column_count] # appends the dictionary with the header of the column and the value of the associated column in this row
                    column_count += 1
                list.append(dict) # appends this row dictionary to the list of rows
                row_count += 1
    if not list:
        list = headers
    return list # returns the csv file as a list of dictionaries of the rows contents

def csvToDictsAppendHeader(path, headerList):
    headers = headerList
    list = [] # initialize a list for the rows in the csv file. Indices are dictionaries with the rows contents
    with open(path, ) as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        row_count = 0
        for row in reader: # iterates through the rows in the csv file
            dict = {} # initializes a dictionary to hold the contents of the csv row
            column_count = 0
            for i in row: # iterates through the columns of the current row
                dict[headers[column_count]] = row[column_count] # appends the dictionary with the header of the column and the value of the associated column in this row
                column_count += 1
            list.append(dict) # appends this row dictionary to the list of rows
            row_count += 1
    if not list:
        list = headers
    return list # returns the csv file as a list of dictionaries of the rows contents

def compareCSVs(path1, path2):
    dict1 = csvToDicts(path1)
    dict2 = csvToDictsAppendHeader(path2, HOSTSCSVHEADERS)

    for i in dict2:
        for k, v in i.items():
            if k == "IPAddress":
                print(f"OK IP {v}")
                IPAddress = v
            if k == "MACAddress":
                print(f"OK MAC {v}")
                MACAddress = v

            
        serialNumber = getSerial(IPAddress)

        for g in dict1:
            for k, v in g.items():
                if k == "SerialNumber":
                    print(f"OK SERIAL {v}")
                    if v == serialNumber:
                        print("Adding IP and MAC")
                        g["IPAddress"] = IPAddress
                        g["MACAddress"] = MACAddress

    return dict1


def writeCSVFromDictList(path, dictList):
    dictionaries = dictList
    keys = dictionaries[0].keys()

    a_file = open(path, "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dictionaries)
    a_file.close()

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


def parseSerial(data):
    data = data.strip('y 01 ')
    if data.startswith("OK"):
        data = data.strip("OK")
    elif data.startswith("NG"):
        data = data.strip("NG")
    else:
        print('error with return code OK/NG')
    return data.rstrip(data[-1])


def getSerial(ip):
    return parseSerial(send_command(ip, 'fy 01 ff\r', PORT))


def fullScreen(func):

    for i in range(52, 68):
        if i == 52:
            input = INPUT_HDMI
        else:
            input = INPUT_DP
        for k, v in TILEFULL.items():
            if str(i) == k:
                x = v
                
                tilecmd = f'di 01 {x}'
        dev = f'10.228.37.{i}'
        send_command(dev, input, PORT)
        send_command(dev, VWFULL, PORT)
        send_command(dev, tilecmd, PORT)
    func()


def twoXtwo():
    for i in range(52, 63):
        for k, v in TILE2X2.items():
            if str(i) == k:
                x = v
                
                tilecmd = f'di 01 {x}'
                dev = f'10.228.37.{i}'
                if str(i) in INPUT2X2:
                    input = INPUT_HDMI
                else:
                    input = INPUT_DP
                send_command(dev, input, PORT)
                send_command(dev, VW2X2, PORT)
                send_command(dev, tilecmd, PORT)
                    
def sendAll(cmd):
    if cmd == POWER_OFF:
        videowall = reversed(VIDEOWALL)
        sleep = 0
    else:
        videowall = VIDEOWALL
        sleep = 3
    #for dev in videowall:
    #    send_command(dev, cmd, PORT)
    #    time.sleep(sleep)
    for i in TVS:
        send_command(i, cmd, PORT)

def configureDevs(pathToConfig):

    devs = csvToDicts(pathToConfig)
    
    for dev in devs:
        for k, v in dev.items():
            if k == "IPAddress":
                d = v
            if k == "NewIPAddress":
                ip = v
            if k == "Subnet":
                subnet = v
            if k == "Gateway":
                gateway = v

        #commands = [SET_TIME_AUTO, NO_SIGNAL_POWER_OFF_OFF, DPM_STANDBY_MODE_OFF, PM_NETWORK_READY, LAN_DAISEY_CHAIN_ON]
        commands = [INPUT_DP]
        for command in commands:
            if d != "10.228.37.55" or "10.228.37.57":
                print(send_command(d, command, PORT))

def scanInversionFrameControl():
    for i in TCC_EVEN_ROWS:
        send_command(i, SCAN_INVERSION_ON, PORT)
    for i in TCC_ODD_ROWS:
        send_command(i, FRAME_CONTROL_ON, PORT)