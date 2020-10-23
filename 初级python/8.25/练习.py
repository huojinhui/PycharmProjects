import requests, selenium
# QQ空间登陆
url = 'https://user.qzone.qq.com/2764855980/infocenter'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'cookie': '2764855980_todaycount=0; 2764855980_totalcount=2712; zzpaneluin=; zzpanelkey=; pgv_pvi=9527743488; pgv_si=s55353344; _qpsvr_localtk=0.01245321639080088; pgv_pvid=3580105475; pgv_info=ssid=s3437041702; ptui_loginuin=1130821644; pt_sms_phone=184******26; uin=o2764855980; skey=@7C0yiBphs; RK=KOTVOoqj7v; ptcz=23e460497bf2faf11aa9185695d2edfc45dd787281b1a5cdd177a614a26d6315; p_uin=o2764855980; pt4_token=D-eCKuKY78GFlhfx9VbXrzrOvnjGD*sEcHMPcd7iPKQ_; p_skey=M9Q5wESSPyfN3VnX*KTrIz5eGFOAeApIOXaPWFOWjY8_; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=12'
}
respose = requests.get(url, headers=headers)
with open('QQ空间.html', 'w', encoding='utf-8') as file:
    file.write(respose.text)