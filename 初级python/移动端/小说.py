import csv
import requests
import random
import json
import pymysql
import time
from lxml import etree
allResult = []
# 从json文件当中获取当前的数据条数以及总数据
# with open('小说.json','r',encoding='utf-8') as file:
# with open('小说test.json','r',encoding='utf-8') as file:
#     # jsonDic = json.load(file)
#     count = jsonDic['count']
#     allResult = jsonDic['data']
db = pymysql.connect('localhost', 'root', 'root', 'python', 8889)
cursor = db.cursor()
count = 0
for i in range(1, 600):
    url = "https://api.hongdouyuedu.com/honor/category/info?category=%E5%A5%B3%E9%A2%91%3B%E7%8E%B0%E4%BB%A3%E8%A8%80%E6%83%85%3B%E6%80%BB%E8%A3%81%E8%B1%AA%E9%97%A8&channel=oppo&device_name=PDPM00&identifier=&physic_size=6.56&platform=wwa1&plattype=aphone&scale_screen=2400_1080&ts=1598649593222&uuid=FF91EABB42C32DD1CBC71BCE6A528208&version=2.5.9&virtual=0&sig=b221f5e56806176a35b9d433da5014bc"
    parameter = {"page_index": i}
    headers = {
        "User-Agent": "okhttp/3.12.1",
        "Host": "api.hongdouyuedu.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "identity",
    }
    response = requests.get(url, headers=headers, params=parameter)
    print(response.text)
    content = response.json()["data"]["data"]
    for book in content:
        print()
        print("开始爬取下一本小说")
        book_name = book["name"]
        print(book_name)
        author_name = book["author_name"]
        print(author_name)
        tags = book["label_name"]
        print(tags)
        categories = book["category_name"]
        print(categories)
        intro = book["described"]
        print(intro)
        words_num = book["words_total"]
        popularity = book["views_total"]
        print(book_name + " 小说爬取完毕")

        # 分享链接
        # share_url = secondary_content["data"]["share_url"]
        share_url = "空"

        dic = {
            '书名': book_name,
            '作者名': author_name,
            '标签': tags,
            '可选分类': categories,
            '简介': intro,
            '字数': words_num,
            '人气数': popularity,
            '分享链接': share_url
        }

        count += 1
        allResult.append(dic)
        # 写入json文件，"红豆小说1000本总裁文.json"
        data = {'data': allResult, 'count': count}
        with open('小说.json', 'w', encoding='utf-8') as file:
            # 直接存入json
            json.dump(data, file, ensure_ascii=False, indent=4)

        count += 1
        # 写入csv文件，"红豆小说1000本总裁文.csv"
        header = ['书名', '作者名', '标签', '可选分类', '简介', '字数', '人气数', '分享链接']
        with open('小说.csv', 'a', encoding='utf-8-sig', newline='') as file:
            huo = csv.DictWriter(file, header)
            if count == 1:
                huo.writeheader()
            huo.writerow(dic)

        # 写入数据库表
        sql = "INSERT INTO xiaoshuo (book_name, author_name, tags, categories, intro, words_num, popularity, share_url) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (
            book_name, author_name, tags, categories, intro, words_num, popularity, share_url)
        cursor.execute(sql)
        # 数据库提交操作
        db.commit()

# 从json文件当中获取当前的数据条数以及总数据
# with open('小说.json','r',encoding='utf-8') as file:
# with open('小说test.json','r',encoding='utf-8') as file:
#     # jsonDic = json.load(file)
#     count = jsonDic['count']
#     allResult = jsonDic['data']

# 关闭数据库
db.close()
