import time
import requests as req
import os
import sys
from colorama import Style, Fore
from rich import print as printf

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

tor = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

enabled = '[rgb(0,255,0)] Enabled [/]'

while True:

    krampus = '''
                        ▄ •▄ ▄▄▄   ▄▄▄· • ▌ ▄ ·.  ▄▄▄·▄• ▄▌.▄▄ ·   ▪   ▄▄▄·  ▄▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
                        █▌▄▌▪▀▄ █·▐█ ▀█ ·██ ▐███▪▐█ ▄██▪██▌▐█ ▀.   ██ ▐█ ▄█  ▀•██ ▀▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
                        ▐▀▀▄·▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█· ██▀·█▌▐█▌▄▀▀▀█▄  ▐█· ██▀·    ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
                        ▐█.█▌▐█•█▌▐█▪ ▐▌██ ██▌▐█▌▐█▪·•▐█▄█▌▐█▄▪▐█  ▐█▌▐█▪·•    ▐█▌·▐█•█▌▐█▪ ▐▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
                        ·▀  ▀.▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀.▀    ▀▀▀  ▀▀▀▀   ▀▀▀.▀       ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
    '''
    
    printf(f'[rgb(40,0,255)]{krampus}[/]')

    time.sleep(0.5) 

    printf('[rgb(40,0,255)] [ ! ] - Made by: Kr4mp1us.py')

    time.sleep(0.5)

    printf(f'[rgb(40,0,255)] [ ^ ] - Tor Proxy: {enabled}. [/]')

    time.sleep(0.5)

    printf('[rgb(40,0,255)] [ - ] - Support: Termux & Linux.')

    time.sleep(0.5)

    printf('[rgb(40,0,255)] [ ? ] - Supporting collection of domain ( ex: google.com ) information and IPV4 and IPV6 addresses.')

    time.sleep(0.5)

    target = str(input(Style.BRIGHT + Fore.LIGHTRED_EX + '[ = ] - Enter the target IP ( or domain, ex: google.com ) address: '))

    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'[ ! ] - Right, the target {target} is being verified and its information obtained..')

    time.sleep(1)

    API = req.get(f'http://ip-api.com/json/{target}', proxies=tor).json()

    clear()

    printf(f'[rgb(40,0,255)]{krampus}[/]')
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ = ] - Status:', API.get('status'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ ! ] - IP:', API.get('query'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ / ] - Country:', API.get('country'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ ~ ] - Country Code:', API.get('countryCode'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ - ] - Region:', API.get('regionName'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ + ] - Region Code:', API.get('region'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ > ] - City:', API.get('city'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ $ ] - ZIP:', API.get('zip'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ * ] - Latitude:', API.get('lat'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ < ] - Longitude:', API.get('lon'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ @ ] - Timezone:', API.get('timezone'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ # ] - ISP:', API.get('isp'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ \ ] - ORG:', API.get('org'))
    time.sleep(0.2)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + '[ % ] - AS:', API.get('as'))
    time.sleep(0.5)

    perg1 = str(input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + ' [ ? ] - Would you like to analyze another target? ( y/n ): '))

    if perg1 == 'y':
        clear()
        continue
    elif perg1 == 'n':
        clear()
        sys.exit()
    else:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + 'ERROR: JUST USE y AND n AS ANSWERS!!!!!!!!')
        time.sleep(2)
        clear()
        sys.exit()
