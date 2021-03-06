import argparse
import re
import requests
import socket
import time

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device')
parser.add_argument('-i', '--inFile')
parser.add_argument('-D', '--domain')
parser.add_argument('-w', '--wait')
parser.add_argument('--creds', action='store_true')
parser.add_argument('-r', '--reboot', action='store_true')
parser.add_argument('-p', '--password', action='store_true')
parser.add_argument('-u', '--username', action='store_true')

args = parser.parse_args()

devs = []
domain = ""
UNAME = args.username
PW = args.password
wait = 1


def checkStatusCode(code):
    if code == 200:
        print(f'[+] Success: {code}')
    else:
        print(f'[x] error: {code}')


def login(dev, uname, pw):
    url = f"http://{dev}/aj.html?a=command&cmd=check_login&p1={uname}&p2={pw}&_=1640107458500"

    payload={}
    headers = {
    'Host': f'{dev}',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': f'http://{dev}/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    checkStatusCode(response.status_code)


def set_uname(dev, uname):
    print(f'[*] setting {dev} username to {uname}')
    url = f"http://{dev}/aj.html?a=command&cmd=SETUNAME&p1={uname}&_=1640107458555"

    payload={}
    headers = {
    'Host': f'{dev}',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': f'http://{dev}/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    checkStatusCode(response.status_code)


def set_pw(dev, pw):
    print(f'[*] setting {dev} password to {pw}')
    url = f"http://{dev}/aj.html?a=command&cmd=SETPW&p1={pw}&_=1640107458556"

    payload={}
    headers = {
    'Host': f'{dev}',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': f'http://{dev}/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    checkStatusCode(response.status_code)

def reboot(dev):

    print(f'[*] rebooting {dev}')
    url = f"http://{dev}/aj.html?a=command&cmd=REBOOT&_=1640626472170"

    payload={}
    headers = {
    'Host': f'{dev}',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': f'http://{dev}/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    checkStatusCode(response.status_code)


def getHostName(dev, domain):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",dev):
        return socket.gethostbyaddr(dev)
    else:
        dev = dev + domain
        return socket.gethostbyname(dev)


def setCreds(devs):
    for d in devs:
        set_uname(d, UNAME)
        set_pw(d, PW)
        time.sleep(wait)


if args.wait:
    wait = args.wait
if args.domain:
    domain = '.' + args.domain
if args.device:
    d = getHostName(args.device, domain)
    devs.append(d)
if args.inFile:
    with open(args.inFile, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            devs.append(getHostName(line.strip(), domain))
if args.creds:
    setCreds(devs)
if args.reboot:
    for d in devs:
        reboot(d)
