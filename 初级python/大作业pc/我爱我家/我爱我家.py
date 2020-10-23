import requests, re
from lxml import etree
alldate = []
url = 'https://bj.5i5j.com/zufang/501065634.html?wscckey=c1bbe581040773d5_1598338385'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Cookie': 'pc_pmf_group_bj=145b35fbda9cdfb21e64efbaadaa71b89fb08a051214e9cdcdf66c863626f275a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22pc_pmf_group_bj%22%3Bi%3A1%3Bs%3A194%3A%22%7B%22pmf_group%22%3A%22baidu%22%2C%22pmf_medium%22%3A%22cpc%22%2C%22pmf_plan%22%3A%22%5Cu7ee9%5Cu6548%5Cu8bcd%22%2C%22pmf_unit%22%3A%22%5Cu79df%5Cu623f%5Cu901a%5Cu7528%5Cu8bcd%5Cu667a%5Cu80fd%5Cu6838%5Cu5fc3%22%2C%22pmf_keyword%22%3A%22%5Cu79df%5Cu623f%5Cu5b50%22%2C%22pmf_account%22%3A%2236%22%7D%22%3B%7D; _ga=GA1.2.298360397.1598329849; _gid=GA1.2.1918993614.1598329849; yfx_c_g_u_id_10000001=_ck20082512305012351145537535587; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3Awww.baidu.com%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; __TD_deviceId=PJU9B53D7RSOOH2K; _dx_uzZo5y=8d4f240e84a62003aed0475acc17b28b640ff6c02fd1845e4c9e0b9dd2f9642dc740fa6f; gr_user_id=69afd72e-1a49-4205-86a6-000b59d7d305; smidV2=20200825123050239be3956f11888d31bcfb47dfc6d97a00e13d0f562a0d270; grwng_uid=a1a81133-9487-408c-a715-d32c9d7e75a3; _Jo0OQK=1F9FBD23B71D75977CABF3C2C355CDC2E9F44687DDDD916CBBD4051E67D25F9D15717F63D96700F00FC8D563D69168EA24CA0CA13DD752BC46F5EBC0F4F3DEAAFF1C57212F12283777C840763663251ADEB840763663251ADEB6D35FF8052C8F2F72350674422DE2517GJ1Z1aQ==; isClose=yes; baidu_OCPC_pc=81d9188ad42b983db2c0c819e87ddff7c24208990eed7c55ac4663606f5ae308a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22baidu_OCPC_pc%22%3Bi%3A1%3Bs%3A438%3A%22%22https%3A%5C%2F%5C%2Fbj.5i5j.com%5C%2Fzufang%3Fpmf_group%3Dbaidu%26pmf_medium%3Dcpc%26pmf_plan%3D%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%26pmf_unit%3D%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%26pmf_keyword%3D%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%26pmf_account%3D36%26pmf_id%3D158108809462%26jzl_kwd%3D158108809462%26jzl_ctv%3D35858745263%26jzl_mtt%3D1%26jzl_adt%3Dcl1%26jzl_ch%3D11%26jzl_act%3D2944626%26jzl_cpg%3D121227748%26jzl_adp%3D4560232160%26jzl_sty%3D50%26jzl_dv%3D1%26bd_vid%3D9400704726135447640%22%22%3B%7D; yfx_mr_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E5%25AD%2590%3A%3A%3A%3A158108809462%3A%3A%3A%3A%25E7%25BB%25A9%25E6%2595%2588%25E8%25AF%258D%3A%3A%25E7%25A7%259F%25E6%2588%25BF%25E9%2580%259A%25E7%2594%25A8%25E8%25AF%258D%25E6%2599%25BA%25E8%2583%25BD%25E6%25A0%25B8%25E5%25BF%2583%3A%3A36%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; PHPSESSID=7lcn6mv244a2ds2on0b4a275m8; domain=bj; yfx_f_l_v_t_10000001=f_t_1598329850216__r_t_1598329850216__v_t_1598338028559__r_c_0; 8fcfcf2bd7c58141_gr_session_id=bc90ee44-5316-496f-b98a-0fe607842061; 8fcfcf2bd7c58141_gr_session_id_bc90ee44-5316-496f-b98a-0fe607842061=true; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1598329851,1598330107,1598338030; zufang_BROWSES=90232234%2C90176771%2C90176770%2C501059040%2C501064176%2C501057585%2C501062471; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1598338432'
}
response = requests.get(url, headers=headers)
with open('一间房.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
# print(response.text)
html = etree.HTML(response.text)
residential_quarters = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[1]/a/text()')[0]
print(residential_quarters)
building_type = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[2]/text()')[0]
print(building_type)
elevator = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[3]/text()')[0]
print(elevator)
rental_mode = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[4]/text()')[0]
print(rental_mode)
if rental_mode != '自供暖':
    open_home = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/text()')[0]
    print(open_home)
    region = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[6]/a[1]/text()')[0]
    print(region)
    unit_structure = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[7]/text()')[0]
    print(unit_structure)
    agency_fee = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[8]/text()')[0]
    print(agency_fee)
    subway = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[9]/a/text()[1]')[0]
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
else:
    rental_mode = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[5]/text()')[0]
    print(rental_mode)
    open_home = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[6]/text()')[0]
    print(open_home)
    region = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[7]/a[1]/text()')[0]
    print(region)
    unit_structure = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[8]/text()')[0]
    print(unit_structure)
    agency_fee = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[9]/text()')[0]
    print(agency_fee)
    subway = html.xpath('/html/body/div[5]/div[2]/div[2]/div[2]/ul/li[10]/a/text()[1]')[0]
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
    '楼型': building_type,
    '电梯': elevator,
    '出租方式': rental_mode,
    '看房时间': open_home,
    '区域': region,
    '户型结构': unit_structure,
    '中介费': agency_fee,
    '地铁': subway,
    '租金': rent,
    '支付方式': payment_method,
    '房间大小': size,
    '厅室': hall,
    '楼层': floor
}
print(dic)