import re, requests, csv, json, pymysql,time
from lxml import etree
alldate = []
num = 0
url = 'https://www.julive.com/project/20061571.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    # 'Cookie': 'GUID=b02dea38-ee1f-44bf-bded-3d640d698ef0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=XFa_1Wc7xMXb8fUUjaj3JXpdtEqo1Mr4mFR0VtZRfbu&wd=&eqid=bc7a0e2f000d164a000000035f460b7e; UM_distinctid=174299cfbbb8c-01d8a844548788-5a472316-1fa400-174299cfbbe86; CNZZDATA5647345=cnzz_eid%3D965041889-1598423450-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1598423450; Hm_lvt_9793f42b498361373512340937deb2a0=1598425988; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22b02dea38-ee1f-44bf-bded-3d640d698ef0%22%2C%22%24device_id%22%3A%22174299cfc601c9-045cfefcbc300d-5a472316-2073600-174299cfc61d5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1598426044'
}
response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# with open('新房.html', 'w', encoding='utf-8') as file:
#     file.write(response.text)
# print(response.text)
html = etree.HTML(response.text)
price = html.xpath('//div[@class="txt"]/span/em/text()')[0]
total_price = html.xpath('//div[@class="txt clearfix"]/span/text()')[0]
type = html.xpath('//p[@class="txt"]/span/a/text()')[0]
adrees = html.xpath('//p[@class="txt href_map"]/span/a/text()')[0]
recent_opening = html.xpath('//p[@class="txt-address"]/span/text()')[0]
name = html.xpath('//div[@class="name-left"]/h1/text()')[0]
tellphone = html.xpath('//div[@class="name-right"]/text()')[0]
tell = url
print(tell)
dic = {
    '单价': price,
    '总价': total_price,
    '类型': type,
    '地址': adrees,
    '开盘时间': recent_opening,
    '小区名字': name,
    '热线': tellphone,
    '链接网址': tell
}
alldate.append(dic)

# csv持久化
header = ['单价', '总价', '类型', '地址', '开盘时间', '小区名字', '热线', '链接网址']
with open('居里新房.csv', 'a', encoding='utf-8-sig', newline='') as file:
    huo = csv.DictWriter(file, header)
    if num == 1:
        huo.writeheader()
    huo.writerow(dic)

 # 写入mysql
db = pymysql.connect('localhost', 'root', '', '123')
cursor = db.cursor()
sql = "INSERT INTO new_house (price,total_price, type, adrees, recent_opening, name, tellphone, tell) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');"%(dic['单价'], dic['总价'], dic['类型'], dic['地址'], dic['开盘时间'], dic['小区名字'], dic['热线'], dic['链接网址'])
cursor.execute(sql)