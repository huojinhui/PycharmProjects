import requests, re, random, csv, pymysql, json, time
from lxml import etree
list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60', 'Opera/8.0 (Windows NT 5.1; U; en)', 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0','Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10']
alldate = []
num = 150
for i in range(6, 101):
    time.sleep(1)
    url = 'https://sh.5i5j.com/zufang/n{}'.format(i)
    headers = {
        'User-Agent': random.choice(list)
        # 'Cookie': 'pc_pmf_group_bj=145b35fbda9cdfb21e64efbaadaa71b89fb08a051214e9cdcdf66c863626f275a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22pc_pmf_group_bj%22%3Bi%3A1%3Bs%3A194%3A%22%7B%22pmf_group%22%3A%22baidu%22%2C%22pmf_medium%22%3A%22cpc%22%2C%22pmf_plan%22%3A%22%5Cu7ee9%5Cu6548%5Cu8bcd%22%2C%22pmf_unit%22%3A%22%5Cu79df%5Cu623f%5Cu901a%5Cu7528%5Cu8bcd%5Cu667a%5Cu80fd%5Cu6838%5Cu5fc3%22%2C%22pmf_keyword%22%3A%22%5Cu79df%5Cu623f%5Cu5b50%22%2C%22pmf_account%22%3A%2236%22%7D%22%3B%7D; _ga=GA1.2.298360397.1598329849; _gid=GA1.2.1918993614.1598329849; yfx_c_g_u_id_10000001=_ck20082512305012351145537535587; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3Awww.baidu.com%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; __TD_deviceId=PJU9B53D7RSOOH2K; _dx_uzZo5y=8d4f240e84a62003aed0475acc17b28b640ff6c02fd1845e4c9e0b9dd2f9642dc740fa6f; gr_user_id=69afd72e-1a49-4205-86a6-000b59d7d305; smidV2=20200825123050239be3956f11888d31bcfb47dfc6d97a00e13d0f562a0d270; grwng_uid=a1a81133-9487-408c-a715-d32c9d7e75a3; _Jo0OQK=1F9FBD23B71D75977CABF3C2C355CDC2E9F44687DDDD916CBBD4051E67D25F9D15717F63D96700F00FC8D563D69168EA24CA0CA13DD752BC46F5EBC0F4F3DEAAFF1C57212F12283777C840763663251ADEB840763663251ADEB6D35FF8052C8F2F72350674422DE2517GJ1Z1aQ==; isClose=yes; baidu_OCPC_pc=81d9188ad42b983db2c0c819e87ddff7c24208990eed7c55ac4663606f5ae308a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22baidu_OCPC_pc%22%3Bi%3A1%3Bs%3A438%3A%22%22https%3A%5C%2F%5C%2Fbj.5i5j.com%5C%2Fzufang%3Fpmf_group%3Dbaidu%26pmf_medium%3Dcpc%26pmf_plan%3D%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%26pmf_unit%3D%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%26pmf_keyword%3D%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%26pmf_account%3D36%26pmf_id%3D158108809462%26jzl_kwd%3D158108809462%26jzl_ctv%3D35858745263%26jzl_mtt%3D1%26jzl_adt%3Dcl1%26jzl_ch%3D11%26jzl_act%3D2944626%26jzl_cpg%3D121227748%26jzl_adp%3D4560232160%26jzl_sty%3D50%26jzl_dv%3D1%26bd_vid%3D9400704726135447640%22%22%3B%7D; yfx_mr_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3A%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; PHPSESSID=7lcn6mv244a2ds2on0b4a275m8; domain=bj; yfx_f_l_v_t_10000001=f_t_1598329850216__r_t_1598329850216__v_t_1598338028559__r_c_0; 8fcfcf2bd7c58141_gr_session_id=bc90ee44-5316-496f-b98a-0fe607842061; 8fcfcf2bd7c58141_gr_session_id_bc90ee44-5316-496f-b98a-0fe607842061=true; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1598329851,1598330107,1598338030; zufang_BROWSES=90232234%2C90176771%2C90176770%2C501059040%2C501064176%2C501057585%2C501062471; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1598338432'
    }
    response = requests.get(url, headers=headers)
    # with open('caogao.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)
    html = etree.HTML(response.text)
    websize = html.xpath('//li/div[@class="listImg"]/a/@href')
    print(websize)

    for j in websize:
        time.sleep(2)
        url = 'https://sh.5i5j.com{}'.format(j)
        headers = {
            'User-Agent': random.choice(list)
            # 'Cookie': '_ga=GA1.2.298360397.1598329849; _gid=GA1.2.1918993614.1598329849; yfx_c_g_u_id_10000001=_ck20082512305012351145537535587; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3Awww.baidu.com%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; __TD_deviceId=PJU9B53D7RSOOH2K; _dx_uzZo5y=8d4f240e84a62003aed0475acc17b28b640ff6c02fd1845e4c9e0b9dd2f9642dc740fa6f; gr_user_id=69afd72e-1a49-4205-86a6-000b59d7d305; smidV2=20200825123050239be3956f11888d31bcfb47dfc6d97a00e13d0f562a0d270; grwng_uid=a1a81133-9487-408c-a715-d32c9d7e75a3; yfx_mr_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3A%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; zufang_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fzufang%252F_%2525E9%2525A6%2525A8%2525E9%252580%25259A%2525E5%2525AE%2525B6%2525E5%25259B%2525AD%253Fzn%253D%2525E9%2525A6%2525A8%2525E9%252580%25259A%2525E5%2525AE%2525B6%2525E5%25259B%2525AD%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E9%25A6%25A8%25E9%2580%259A%25E5%25AE%25B6%25E5%259B%25AD%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; PHPSESSID=44dtiqfmeb75rdmlv7bmqab5h2; domain=bj; pc_pmf_group_bj=145b35fbda9cdfb21e64efbaadaa71b89fb08a051214e9cdcdf66c863626f275a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22pc_pmf_group_bj%22%3Bi%3A1%3Bs%3A194%3A%22%7B%22pmf_group%22%3A%22baidu%22%2C%22pmf_medium%22%3A%22cpc%22%2C%22pmf_plan%22%3A%22%5Cu7ee9%5Cu6548%5Cu8bcd%22%2C%22pmf_unit%22%3A%22%5Cu79df%5Cu623f%5Cu901a%5Cu7528%5Cu8bcd%5Cu667a%5Cu80fd%5Cu6838%5Cu5fc3%22%2C%22pmf_keyword%22%3A%22%5Cu79df%5Cu623f%5Cu5b50%22%2C%22pmf_account%22%3A%2236%22%7D%22%3B%7D; baidu_OCPC_pc=81d9188ad42b983db2c0c819e87ddff7c24208990eed7c55ac4663606f5ae308a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22baidu_OCPC_pc%22%3Bi%3A1%3Bs%3A438%3A%22%22https%3A%5C%2F%5C%2Fbj.5i5j.com%5C%2Fzufang%3Fpmf_group%3Dbaidu%26pmf_medium%3Dcpc%26pmf_plan%3D%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%26pmf_unit%3D%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%26pmf_keyword%3D%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%26pmf_account%3D36%26pmf_id%3D158108809462%26jzl_kwd%3D158108809462%26jzl_ctv%3D35858745263%26jzl_mtt%3D1%26jzl_adt%3Dcl1%26jzl_ch%3D11%26jzl_act%3D2944626%26jzl_cpg%3D121227748%26jzl_adp%3D4560232160%26jzl_sty%3D50%26jzl_dv%3D1%26bd_vid%3D9400704726135447640%22%22%3B%7D; yfx_f_l_v_t_10000001=f_t_1598329850216__r_t_1598454812388__v_t_1598494741822__r_c_2; 8fcfcf2bd7c58141_gr_session_id=baf05a05-745d-4c5f-903b-9c7018dd136e; _Jo0OQK=9ACFBD23B71D75977CABF3C2C355CDC2E9F44687DDDD916CBBD4051E67D25F9D15717F63D96700F00FC8D563D69168EA24CB965485A791FA2916DD0B8F2CAAC6ABAC57212F12283777C840763663251ADEB840763663251ADEB86227F44363BA5389547054735CB82A9GJ1Z1fA==; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1598356571,1598405084,1598443454,1598494743; 8fcfcf2bd7c58141_gr_session_id_baf05a05-745d-4c5f-903b-9c7018dd136e=true; zufang_BROWSES=90232234%2C90176771%2C90176770%2C501059040%2C501064176%2C501057585%2C501062471%2C501050736%2C501065526%2C501057632%2C501059342%2C501058958%2C44510955%2C44610823%2C43841261%2C43224101%2C44612462%2C44603837%2C44614521%2C44635206%2C43807520%2C44651387%2C44625985%2C501064984%2C501061890; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1598494830'
        }
        response = requests.get(url, headers=headers)
        with open('一间房.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        # print(response.text)
        html = etree.HTML(response.text)
        residential_quarters = html.xpath('//div[@class="zushous"]/ul/li[@gio-trace="tracegio_bi"]/a/text()')
        if len(residential_quarters) == 0:
            residential_quarters = '无'
            print(residential_quarters)
        else:
            residential_quarters = html.xpath('//div[@class="zushous"]/ul/li[@gio-trace="tracegio_bi"]/a/text()')[0]
            print(residential_quarters)
        rental_mode = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[2]/text()')
        if len(rental_mode) <= 0:
            rental_mode = ['无'][0]
        else:
            rental_mode = rental_mode[0]
        print(rental_mode)
        open_home = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[3]/text()')
        if len(open_home) == 0:
            open_home = '无'
            print(open_home)
        else:
            open_home = open_home[0]
            print(open_home)
        region = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[4]/a[1]/text()')
        if len(region) == 0:
            region = '无'
            print(region)
        else:
            region = region[0]
            print(region)
        subway = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/a/text()[1]')
        if len(subway) == 0:
            subway = '无'
            print(subway)
        else:
            subway = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/a/text()[1]')[0]
            print(subway)
        rent = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p/span[1]/text()')[0]
        print(rent)
        payment_method = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/div/p/span[2]/text()[2]')[0]
        print(payment_method, type(payment_method))
        size = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[2]/div/p[1]/text()')[0]
        print(size)
        hall = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/p[1]/text()')[0]
        print(hall)
        floor = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]/div/p[2]/text()')[0]
        print(floor)
        dic = {
            '小区': residential_quarters,
            '出租方式': rental_mode,
            '看房时间': open_home,
            '区域': region,
            '地铁': subway,
            '租金': rent,
            '支付方式': payment_method,
            '房间大小': size,
            '厅室': hall,
            '楼层': floor
        }
        print(dic)
        alldate.append(dic)
        date = {'date': alldate}
        with open('我爱我家.json', 'w', encoding='utf-8') as file:
            # 直接存入json
            json.dump(date, file, ensure_ascii=False, indent=4)


        # csv数据持久化
        header = ['小区', '出租方式', '看房时间', '区域', '地铁', '租金', '支付方式', '房间大小', '厅室', '楼层']
        with open('我爱我家.csv', 'a', encoding='utf-8-sig', newline='') as file:
            huo = csv.DictWriter(file, header)
            if num == 1:
                huo.writeheader()
            huo.writerow(dic)

            # 写入mysql
            db = pymysql.connect('localhost', 'root', '', '123')
            cursor = db.cursor()
            sql = "INSERT INTO home (residential_quarters,rental_mode, open_home, region, subway, rent, payment_method, size, hall, floor) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s');" %(dic['小区'], dic['出租方式'], dic['看房时间'], dic['区域'], dic['地铁'], dic['租金'], dic['支付方式'], dic['房间大小'], dic['厅室'], dic['楼层'])
            cursor.execute(sql)
            num += 1
            print('第{}间信息处理完'.format(num))

    with open('我爱我家.json', 'r', encoding='utf-8') as file:
        dic = json.load(file)
        alldate = dic['date']

# print(alldate)
