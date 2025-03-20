import requests
import time
import sys

# Các màu sắc cho giao diện
den = "\033[1;30m"
xanhla = "\033[1;92m"
do_nhat = "\033[1;91m"
vang_nhat = "\033[1;93m"
xanhduong_sang = "\033[1;94m"
hong_nhat = "\033[1;95m"
trang_sang = "\033[1;97m"
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xanhd = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"

def print_banner():
    banner = f"""\033[1;34m█ \033[1;33mBản Quyền Tool Thuộc:\033[1;31m Thomas Lee\n"""
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

def print_info():
    # Cân chỉnh lại các dòng sao cho các khung viền đều
    print(f"{xanhd}╔════════════════════════════════════════════════════════════════╗")
    print(f"{xanhd}║ {xanhla}Lưu Ý:{trang} Đây Là Chức Năng {do}Random Từ {vang}0-10 Follow{trang} Cho Mỗi Lần Chờ      ║")
    print(f"{xanhd}╚════════════════════════════════════════════════════════════════╝")
    time.sleep(0.5)

print_banner()
time.sleep(0.5)
print_info()

# Nhập UID TikTok
username = input(f"{xanhd}█ {trang}Nhập UID TikTok (Không Nhập @): {do}")
while True:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    # Lấy thông tin session và token
    access = requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
    try:
        session = access.cookies['ci_session']
        headers.update({'cookie': f'ci_session={session}'})
        token = access.text.split("csrf_token = '")[1].split("'")[0]

        # Tạo dữ liệu yêu cầu follow
        data = '{"type":"follow","q":"@' + username + '","google_token":"t","token":"' + token + '"}'
        search = requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()

        # Nếu thành công
        if search['success'] == True:
            data_follow = search['data']
            data = '{"google_token":"t","token":"' + token + '","data":"' + data_follow + '","type":"follow"}'
            send_follow = requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()

            if send_follow['o'] == 'Success!' and send_follow['success'] == True and send_follow['type'] == 'success':
                print(f"{xanhla}  █ {xanhla}Tăng Follow Tik Tok Thành Công")
                continue

            elif send_follow['o'] == 'Oops...' and send_follow['success'] == False and send_follow['type'] == 'info':
                try:
                    thoigian = send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                    phut = thoigian.split(' Minutes')[0]
                    giay = int(phut) * 60
                    for i in range(giay, 0, -1):
                        print(f"{xanhduong_sang}  █ {hong}Thomas Lee{trang} █ {xanhla}Vui Lòng Chờ: {do}{i} {xanhla}Giây", end='\r')
                        time.sleep(1)
                    continue
                except:
                    print(f"{do}Lỗi Không Xác Định               ")
                    continue
    except:
        print(f"{do}Lỗi Không Xác Định               ")
        continue
