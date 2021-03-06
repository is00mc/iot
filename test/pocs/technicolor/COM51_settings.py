import requests
import urllib

dev = ''
baseURL = f'http://{dev}'
target_IP = ''
target_subnet = ''
target_gateway = ''

file = "C:\\Users\\MatthewCampbell\\Box\\Northeast\\Code Archive\\Matt Campbell\\Jobs\\2021\\in_progress\\2105105 - Fanduel Clearwater\\program_files\\technicolor_configs\\Clearwater TVs XML.xml"
#target_xml = "extsourceDesc.xml"
target_xml = "tvs.xml"


def check_status_code(code):
    if code == 200:
        response = 'SUCCESS'
    else:
        response = 'something went wrong'
    return response


def changeIP():
    url = f"{baseURL}/cgi-bin/webcmd?screen=userConfigCardIp&userConfigCardIp={dev}&IP_Address_Configuration=4&Base_IP_Address0={target_IP}&Subnet={target_subnet}&Gateway={target_gateway}&Dns=&Time_To_Live=3&Send_Log_IP_Address=&Log_Level=&NTSC8_IP=&NTSC8_TunerCount=0&Utility_Configuration="

    payload={}
    headers = {
    'Host': f'{dev}',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'{baseURL}/cgi-bin/webcmd?screen=CardEdit?tune=0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

def xml_upload(file, target_xml):
    with open(file, 'r') as reader:
        xml = reader.read()
    content = urllib.parse.quote(xml)

    url = f"{baseURL}/cgi-bin/webcmd?screen=fileSave&name=mt/{target_xml}&append=0&text={content}"
    payload={}
    headers = {
    'Host': f'{dev}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': '*/*',
    'Referer': f'{baseURL}/mt/MTeditor.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return check_status_code(response.status_code)

xml_upload(file, target_xml)
