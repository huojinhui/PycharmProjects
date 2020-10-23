import re
import requests
import csv
import json
import pymysql
import time
from lxml import etree
alldate = []
num = 0
url = 'https://www.17k.com/book/3219236.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Cookie': 'GUID=b02dea38-ee1f-44bf-bded-3d640d698ef0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=XFa_1Wc7xMXb8fUUjaj3JXpdtEqo1Mr4mFR0VtZRfbu&wd=&eqid=bc7a0e2f000d164a000000035f460b7e; UM_distinctid=174299cfbbb8c-01d8a844548788-5a472316-1fa400-174299cfbbe86; CNZZDATA5647345=cnzz_eid%3D965041889-1598423450-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1598423450; Hm_lvt_9793f42b498361373512340937deb2a0=1598425988; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22b02dea38-ee1f-44bf-bded-3d640d698ef0%22%2C%22%24device_id%22%3A%22174299cfc601c9-045cfefcbc300d-5a472316-2073600-174299cfc61d5%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1598426044'
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# with open('小说.html', 'w', encoding='utf-8') as file:
#     file.write(response.text)
# print(response.text)
html = etree.HTML(response.text)
book_name = html.xpath('//div[@class="Props"]/div/a/img/@alt')[0]
level = html.xpath('//div[@class="cont"]//td/span/text()')[0]
book_type = html.xpath('//div[@class="cont"]//td/a/text()')[0]
click_week = html.xpath('//td[@id="weekclickCount"]/text()')[0]
click_mouth = html.xpath('//td[@id="monthclickCount"]/text()')[0]
update_week = html.xpath('//td[@id="hb_week"]/text()')[0]
update_mouth = html.xpath('//td[@id="hb_month"]/text()')[0]
recommend_week = html.xpath('//td[@id="flower_week"]/text()')[0]
recommend_mouth = html.xpath('//td[@id="flower_month"]/text()')[0]
rederse = html.xpath(
    '//div[@class="BookData"]//p/em[@id="howmuchreadBook"]/text()')[0]
word = html.xpath('//div[@class="BookData"]//p/em[@class="red"]/text()')[0]
update_day = html.xpath(
    '//div[@class="BookData"]//p/em[@class="green"]/text()')[0]
print(update_day)
dic = {
    '书名': book_name,
    '授权级别': level,
    '作品类别': book_type,
    '本周点击': click_week,
    '本月点击': click_mouth,
    '本周更新': update_week,
    '本月更新': update_mouth,
    '周推荐票': recommend_week,
    '月推荐票': recommend_mouth,
    '人次': rederse,
    '字数': word,
    '更新天数': update_day
}
alldate.append(dic)
num += 1
# csv持久化
header = [
    '书名',
    '授权级别',
    '作品类别',
    '本周点击',
    '本月点击',
    '本周更新',
    '本月更新',
    '周推荐票',
    '月推荐票',
    '人次',
    '字数',
    '更新天数']
with open('小说.csv', 'a', encoding='utf-8-sig', newline='') as file:
    huo = csv.DictWriter(file, header)
    if num == 1:
        huo.writeheader()
    huo.writerow(dic)

 # 写入mysql
db = pymysql.connect('localhost', 'root', '', '123')
cursor = db.cursor()
sql = "INSERT INTO book (book_name,level, book_type, click_week, click_mouth, update_week, update_mouth, recommend_week, recommend_mouth, rederse, word, update_day) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s');" % (
    dic['书名'], dic['授权级别'], dic['作品类别'], dic['本周点击'], dic['本月点击'], dic['本周更新'], dic['本月更新'], dic['周推荐票'], dic['月推荐票'], dic['人次'], dic['字数'], dic['更新天数'])
cursor.execute(sql)
print('第{}本小说完'.format(num))
