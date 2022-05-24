import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('max_Port')

args = parser.parse_args()

swtPrts = []

def parseSwtPrt(swtPrt):
    port = {}
    split = swtPrt.split('/')
    port[split[0].strip()] = split[2].strip()
    swtPrts.append(port)


with open(args.file, 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        parseSwtPrt(line)

def comparePorts(ports):
    i = 0
    while i < len(ports):
        j = i + 1
        while j < len(ports):
            if ports[i] == ports[j]:
                for k, v in ports[j].items():
                    print(f'[!] duplicate found: {k}/0/{v}')
                j += 1
            else:
                j += 1
        i += 1

def findOpenPorts(maxPorts, usedPorts):
    swtOne = []
    swtTwo = []

    for port in usedPorts:
        for k, v in port.items():
            if k == '1':
                swtOne.append(v)
            elif k == '2':
                swtTwo.append(v)
    print('[*] available ports:')
    i = 1
    while i <= maxPorts:
        if str(i) not in swtOne:
            print(f"1/0/{i}")
        i += 1

    i = 1
    while i <= maxPorts:
        if str(i) not in swtTwo:
            print(f"2/0/{i}")
        i += 1

def main():
    findOpenPorts(int(args.max_Port), swtPrts)
    comparePorts(swtPrts)

main()