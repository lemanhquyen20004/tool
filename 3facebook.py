from time import sleep
import re
import os
import requests
import colorama
colorama.init()
os.system('clear')

def display():
    print("""\033[1;32m╔══════════════════════════════════════════════╗
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

\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\033[1;34m  █ \033[1;33mBản Quyền Tool Thuộc:\033[1;31m Thomas Lee
\033[1;34m  █ \033[1;31mCảm ơn bạn đã sử dụng tool""")
    
def nghigiailao(o):
    while o > 0:
        o -= 1
        print(f"\033[38;5;99m█ [Thomas Lee][Vui Lòng Chờ][{o} Giây]", end='\r')
        sleep(1 / 5)
        print(f"\x1b[38;5;226m█ [Thomas Lee][Vui Lòng Chờ][{o} Giây]", end='\r')
        sleep(1 / 5)
        print(f"\x1b[38;5;207m█ [Thomas Lee][Vui Lòng Chờ][{o} Giây]", end='\r')
        sleep(1 / 5)
        
class Machine:
    def __init__(self):
        self.session = []
        self.delay = 0
        self.url = None
        self.dict_buff = {'1': 'like', '2': 'love', '3': 'care', '4': 'haha', '5': 'wow', '6': 'sad', '7': 'angry'}
        self.list_select = []
        self.headers_buff = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        }

    def enter_cookie(self):
        cookie_input = input("➣\t Nhập Cookie Của Bạn: ")
        with open('cookie.txt', 'w') as f:
            f.write(cookie_input + '\n')
        print("Cookie đã được lưu vào cookie.txt")

    def buff(self, session):
        get_token = session.get('https://machineliker.net/auto-reactions').text
        token = get_token.split('name="_token" value="')[1].split('"')[0]
        hash_ = get_token.split('name="hash" value="')[1].split('"')[0]
        data_buff = {
            'url': self.url,
            'limit': '20',
            'reactions[]': self.list_select,
            '_token': token,
            'hash': hash_
        }
        response = session.post('https://machineliker.net/auto-reactions', headers=self.headers_buff,
                                data=data_buff).text
        if '><strong>Error!</strong>' and "You're currently under cooldown periods, please try again after" in response:
            count = re.findall(r'please try again after (\d+) minutes.</p>', response)[0]
            second = int(count) * 60
            print(f"Sorry Vui Lòng Đợi {second}s Nữa")
            self.delay = second
        elif 'Order Submitted' in response:
            self.dem += 1
            print("\033[1;36m╔═══════════════════════════════════╗")
            print(f"\033[1;36m║\033[1;32m Tăng Thành Công \033[1;31m+20 Cảm Xúc \033[38;5;51m[ \x1b[38;5;226m{self.dem} \033[38;5;51m]")
            print("\033[1;36m╚═══════════════════════════════════╝")
            self.delay = 400
        else:
            print("\033[1;34m  █ \033[1;31mLỗi\033[1;32m Vui Lòng Thoát Tool \033[1;31mChờ 20p Sau \033[1;32mChạy Lại Nhé")

    def main(self):
        self.enter_cookie()  # Yêu cầu người dùng nhập cookie
        self.cookies = open('cookie.txt').read().split("\n")
        
        for ckfb in self.cookies:
            session = requests.Session()
            if ckfb == '':
                break
            a = session.get('https://machineliker.net/login')
            self.headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'vi-VN,vi;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-AU;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'x-xsrf-token': session.cookies.get('XSRF-TOKEN').replace('%3D', '='),
            }
            data = {
                'session': ckfb
            }
            response = session.post('https://machineliker.net/login', headers=self.headers, data=data).json()
            if response['success']:
                name = response['user']['name']
                id_ = response['user']['id']
                print(f"\x1b[38;5;75m\033[1;34m  █ Login Thành Công: \x1b[38;5;46m{id_}\033[0m | \033[1;32m{name} \x1b[38;5;46m")
                
                self.session.append(session)
            else:
                print(f"\033[1;34m  █\033[1;31m Login Thất Bại! Kiểm Tra Lại Cookie Facebook \033[1;32m{ckfb.split('c_user=')[1].split(';')[0]}\033[0m")
        
        self.url = input("\033[1;34m  █ \033[1;37mNhập Link Bài Viết Cần Buff:\033[1;31m ")
        print("\x1b[38;5;46m══" + "══" * 10)
        print("\033[1;34m█ \033[1;33mChọn loại cảm xúc cần buff \033[1;36m[\033[1;31mCó Thể Chọn Nhiều Ví Dụ 123\033[1;36m]")

        select = input("\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn \033[1;37m: \033[1;35m")
        self.list_select = [self.dict_buff[x] for x in select]
        while True:
            for session in self.session:
                self.buff(session)
            nghigiailao(self.delay)


display()
Machine().main()
