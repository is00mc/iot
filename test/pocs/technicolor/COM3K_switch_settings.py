import requests
from requests.models import Response

# COM3K Switch Settings
dev = '192.168.10.2'
baseURL = f'http://{dev}'


def check_status_code(code):
    if code == '200':
        response = 'SUCCESS'
    else:
        response = 'something went wrong'
    return response

def router_port():
    url = f"{baseURL}/config/ipmc"

    payload = "ipmc_mode=on&ssm4_range_prefix=&ssm4_range_length=&router_port_10=on&sid=-1&ipmc_version=1"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '90',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Basic YWRtaW46',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{baseURL}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/ipmc_igmps.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

def igmp_vlan():
    url = f'{baseURL}/config/ipmc_vlan'

    payload = "StartVid=1&NumberOfEntries=20&mvid_ipmc_vlan_0=1&vlan_mode_1=on&vlan_qradr_1=0.0.0.0&sid=-1&ipmc_version=1"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '106',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Basic YWRtaW46',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{baseURL}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/ipmc_igmps_vlan.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

def flow_control():
    url = f"{baseURL}/config/ports"

    payload = "__ctl__3=_none_&__ctl__4=on&__ctl__5=on&__ctl__6=on&__ctl__7=on&__ctl__8=on&__ctl__9=on&__ctl__10=on&__ctl__11=on&__ctl__12=on&__ctl__16=0-7&__ctl__17=10240&__ctl__18=_none_&speed_1=1A1A0A0A0&fdx_1=on&hdx_1=on&speed_10_1=on&speed_100_1=on&speed_1000_1=on&flow_1=on&pfc_range_1=0-7&max_1=10240&speed_2=1A1A0A0A0&fdx_2=on&hdx_2=on&speed_10_2=on&speed_100_2=on&speed_1000_2=on&flow_2=on&pfc_range_2=0-7&max_2=10240&speed_3=1A1A0A0A0&fdx_3=on&hdx_3=on&speed_10_3=on&speed_100_3=on&speed_1000_3=on&flow_3=on&pfc_range_3=0-7&max_3=10240&exc_3=0&speed_4=1A1A0A0A0&fdx_4=on&hdx_4=on&speed_10_4=on&speed_100_4=on&speed_1000_4=on&flow_4=on&pfc_range_4=0-7&max_4=10240&exc_4=0&speed_5=1A1A0A0A0&fdx_5=on&hdx_5=on&speed_10_5=on&speed_100_5=on&speed_1000_5=on&flow_5=on&pfc_range_5=0-7&max_5=10240&exc_5=0&speed_6=1A1A0A0A0&fdx_6=on&hdx_6=on&speed_10_6=on&speed_100_6=on&speed_1000_6=on&flow_6=on&pfc_range_6=0-7&max_6=10240&exc_6=0&speed_7=1A1A0A0A0&fdx_7=on&hdx_7=on&speed_100_7=on&speed_1000_7=on&speed_2500_7=on&flow_7=on&pfc_range_7=0-7&max_7=10240&speed_8=1A1A0A0A0&fdx_8=on&hdx_8=on&speed_100_8=on&speed_1000_8=on&speed_2500_8=on&flow_8=on&pfc_range_8=0-7&max_8=10240&speed_9=1A0A4A1A0&fdx_9=on&hdx_9=on&speed_100_9=on&speed_1000_9=on&speed_2500_9=on&pfc_range_9=0-7&max_9=10240&speed_10=1A1A0A0A0&fdx_10=on&hdx_10=on&speed_100_10=on&speed_1000_10=on&speed_2500_10=on&speed_5g_10=on&speed_10g_cop_10=on&flow_10=on&pfc_range_10=0-7&max_10=10240&speed_11=1A1A0A0A0&fdx_11=on&hdx_11=on&speed_100_11=on&speed_1000_11=on&speed_2500_11=on&speed_5g_11=on&speed_10g_cop_11=on&flow_11=on&pfc_range_11=0-7&max_11=10240&sid=-1"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '1609',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Basic YWRtaW46',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{baseURL}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/ports.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

def save_config():
    url = f"{baseURL}/config/icfg_conf_save"

    payload = "save=0"
    headers = {
    'Host': f'{dev}',
    'Content-Length': '6',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Basic YWRtaW46',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{baseURL}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/icfg_conf_save.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

def reboot_chassis():

    print(f'[*] performing a warm reboot of {dev}')

    url = f"{baseURL}/config/misc"

    payload = "warm="
    headers = {
    'Host': f'{dev}',
    'Content-Length': '5',
    'Cache-Control': 'max-age=0',
    'Authorization': 'Basic YWRtaW46',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{baseURL}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/wreset.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return check_status_code(response.status_code)