from selenium import webdriver
from lxml import etree
import time
import csv
import pymysql
import json
import requests
# 1.使用selenium将致设计的数据爬取5页,并将数据保存为 csv,mysql,json
# 	https://www.zhisheji.com/
header = ['标题', '图片url地址', '类型', '人气数', '点赞数', '评论数', '作者', '作者头像url地址']
# 新建csv文件
with open('致设计.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 创建一个写入对象
    csv_file = csv.DictWriter(file, header)
    # 写入头文件
    csv_file.writeheader()

allList = []

def getdata():
    # 网址
    url = 'https://www.zhisheji.com/'
    # 打开网页
    driver.get(url)
    # 等待20秒
    time.sleep(20)
    # 获取源代码: driver.page_source
    # 把源代码转化为标签类型
    html = etree.HTML(driver.page_source)
    # 取出每一条li标签
    li_list = html.xpath('//ul[@class="list"]/li')
    # 遍历所有li标签
    for li in li_list:
        # 标题
        title = li.xpath('./a/@title')[0]
        # 图片url地址 作者头像url地址
        imgsrc, authorimg = li.xpath('.//img[@class="previews"]/@mysrc')
        # 类型
        type = li.xpath('.//div[@class="desc"]/text()')[0]
        # 人气数 点赞数 评论数
        view, praise, comment = li.xpath('.//em/text()')
        # 作者
        author = li.xpath('.//div[@class="sjs-name"]/a/@title')[0]
        data = {
            '标题': title,
            '图片url地址': imgsrc,
            '类型': type,
            '人气数': view,
            '点赞数': praise,
            '评论数': comment,
            '作者': author,
            '作者头像url地址': authorimg
        }
        # 添加每一条数据到csv中
        with open('致设计.csv', 'a', encoding='utf-8-sig', newline='') as file:
            # 创建一个写入对象
            csv_file = csv.DictWriter(file, header)
            # 写入每一条数据
            csv_file.writerow(data)

        # 存入数据库中
        # sql语句
        sql = "INSERT INTO zhisheji (title,imgsrc,type,view,praise,comment,author,authorimg) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(title,imgsrc,type,view,praise,comment,author,authorimg)
        print(sql)
        # 执行sql语句
        cursor.execute(sql)

        # 存入json
        allList.append(data)
        # 构建json数据
        jsdata = {'data': allList}
        # 写入json数据
        with open('致设计.json', 'w', encoding='utf-8') as file:
            json.dump(jsdata, file, ensure_ascii=False, indent=4)

# 指定对应的浏览器访问网页
driver = webdriver.Chrome('chromedriver.exe')

# 连接到数据库
db = pymysql.connect('localhost', 'root', '', 'python')
# 新建游标对象
cursor = db.cursor()

# 爬取1-5页
for i in range(1,6):
    print('爬取{}'.format(i))
    getdata()
    # 点击对应的页码
    driver.find_element_by_xpath('//*[@id="istj"]/div/div/a[{}]'.format(i)).click()

# 关闭浏览器
driver.quit()
# 提交操作
db.commit()
# 关闭数据库
db.close()



# 2.以所学的selenium知识点,将古诗文网我的模块里面的所有诗爬取出来: (输入验证码)
# https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx