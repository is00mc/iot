import argparse
from os import error
import lg
from termAttributes import TermAttributes # in parent directory may need to update import statement

devices = []
numErrors = 0
errors = []

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', help='ip address or host name of the device to send commands to')
parser.add_argument('-if', '--inFile', help='file containing a list of devices')
parser.add_argument('-l', '--list', action='store_true', help='lists possible commands and their attributes')
parser.add_argument('--send', action='store_true', help='send command to device')
parser.add_argument('-c', '--command', help='command to send to device')
parser.add_argument('-p', '--parameter', help='parameter for command')

args = parser.parse_args()

command = args.command
parameter = args.parameter
print(command)
print(parameter)

if args.list:
    lg.LG.printAttr()
if args.device:
    devices.append(args.device)
if args.inFile:
    with open(args.inFile, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            devices.append(line)
if args.send:
    if not command:
        errors.append(TermAttributes.printText(TermAttributes.error, "No command given to send to device"))
        numErrors += 1
    if not devices:
        errors.append(TermAttributes.printText(TermAttributes.error, "No devices given to send commands to"))
        numErrors += 1
    if numErrors > 0:
        TermAttributes.printText(TermAttributes.error, f"program ran with {numErrors} errors")
        exit()
