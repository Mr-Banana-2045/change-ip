import os
import time
from datetime import datetime
#file txt ip
file = open('C:\Users\M-IT\Desktop\ip.txt')
#banner script
banner = """ 
\033[93m                    |\______/|
                    |  ˣ ‿ ˣ |                 |\___/|
                    |        |    \033[103;94m change IP \033[00m\033[93m  | ˣ‿ˣ |
                    |        |                 |     |\033[92m
 _______           _______  _        _______  _______ _________ _______
(  ____ \|\     /|(  ___  )( (    /|(  ____ \(  ____ \\__   __/(  ____ )
| (    \/| )   ( || (   ) ||  \  ( || (    \/| (    \/   ) (   | (    )|
| |      | (___) || (___) ||   \ | || |      | (__       | |   | (____)|
| |      |  ___  ||  ___  || (\ \) || | ____ |  __)      | |   |  _____)
| |      | (   ) || (   ) || | \   || | \_  )| (         | |   | (
| (____/\| )   ( || )   ( || )  \  || (___) || (____/\___) (___| )
(_______/|/     \||/     \||/    )_)(_______)(_______/\_______/|/  \033[101;93m<var : one>\033[00m
"""
print(banner)
#date
tieme = datetime.now()
date = tieme.strftime("%H:%M:%S")
#start script
for i in range(100):
	time.sleep(10)
	ip = file.readline()
	print(f"\033[93m{date}:\033[00m Your IP has changed > \033[92m{ip}")
	os.system(f"ifconfig eth0 {ip}")