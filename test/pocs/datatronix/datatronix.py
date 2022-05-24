import requests

dev = ''
baseURL = f'http://{dev}'
target_IP = ''
target_subnet = ''
target_gateway = ''
target_hostname = ""


def changeMGMTIP(dev, target_IP, target_subnet, target_gateway, target_hostname, dhcp=0):

    # mgmt ip

    url = f"{baseURL}/info/network.json"

    payload = f"host={target_hostname}&dhcp={dhcp}&ip={target_IP}&sub={target_subnet}&gw={target_gateway}"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '71',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': f'{baseURL}',
    'Referer': f'{baseURL}/protect/network.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def changeStrmIP(dev, target_IP, target_subnet, target_gateway, target_hostname, dhcp=0):
    baseURL = f'http://{dev}'

    # streaming ip

    url = f"{baseURL}/info/selfip.json"

    payload = f"sdhcp={dhcp}&sip={target_IP}&ssub={target_subnet}&sgw={target_gateway}"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '55',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': f'{baseURL}',
    'Referer': f'{baseURL}/protect/network.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def reboot(dev):
    baseURL = f'http://{dev}'

    url = f"{baseURL}/act/reboot.cgi?act=1"

    payload={}
    headers = {
    'Host': f'{dev}',
    'Authorization': 'Basic YWRtaW46QWRtaW4xMjM=',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': f'{baseURL}/protect/reboot.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


changeMGMTIP(dev, target_IP, target_subnet, target_gateway, target_hostname, 0)
reboot(dev)
