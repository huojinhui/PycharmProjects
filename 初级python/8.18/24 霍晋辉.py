import re
# 1.检索邮箱:
# @前面可以有字母数字下划线
# @后面都不能有下划线,可以有数字或者字母
# 21312321@qq.com
# abc@163.com
# hwqeqewyh@aaaedu.cc
# a@sad.com.cc
# abc@wqeq.org
# abc_abc@abc.abc
# a@163.abc
#
# mailbox = ''
# date = ['21312321@qq.com', 'abc@163.com', 'hwqeqewyh@aaaedu.cc', 'a@sad.com.cc', 'abc@wqeq.org', 'abc_abc@abc.abc', 'a@163.abc']
# for i in date:
#     # @前面可以有字母数字下划线  \w{1,}   \w+
#     # @后面都不能有下划线,可以有数字或者字母  [^_]{1,}
#     # 点后面的内容(\.[0-9a-z]{2, 6}){1, 2}
#     pattern = r'^\w{1,}@[^_]{2,10}$'
#     result = re.search(pattern, i)
#     if result:
#         mailbox += i + '  '
# print(mailbox)


# 2.检验身份证号:
# 18位:
# 1位不能是0
# 2-17: 纯数字
# 18: 数字或者x
# id = '14232819972029281x'
# # 1位不能是0  [1-9]{1}
# # 2-17: 纯数字  [0-9]{16}
# # 18: 数字或者x  ([0-9x]{1})   \d|x
# pattern = r'^[^0]{1}[0-9]{16}([0-9]|x{1})$'
# result = re.search(pattern, id)
# if result:
#     print('是身份证号')
# else:
#     print('不是身份证号')

# 3.校验网址
# 	http://www.baidu.com
# 	http://baidu.com
# 	www.baidu.com
# 	https://www.baidu.com
# 	tieba.baidu.com
# 	news.baidu.com
# 	yuan.news.baidu.com
# 	news.baidu.com.cn
# date = ['http://www.baidu.com', 'http://baidu.com', 'www.baidu.com', 'https://www.baidu.com', 'tieba.baidu.com', 'news.baidu.com', 'yuan.news.baidu.com', 'news.baidu.com.cn']
# for i in date:
#     # 点前面是(http://www)|(www)|(https://www)三个中的一个
#     # 点后面是[com]{3}
#
#     # http:// 整体  ?
#     # //后面第一块  [0-9a-z]{3,10}
#     # .字母数字(整体){1, 3}
#     pattern = r'((http://www)|(www)|(https://www))\.baidu\.[com]{3}'
#     result = re.search(pattern, i)
#     if result:
#         print(i)


# 附加题:
# 4.将zhanku.html放在pycharm打开,然后取出每条数据的 作品图片url地址,作品名字,作品类型,人气数,评论数,点赞数,作者
# 如果没有该字段的数据,写无;把数据存入到csv
#
# 作品图片的url地址: <img src="图片的地址">
with open('站酷.html', 'r', encoding='utf-8') as file:
    date = file.read()

# 放所有的信息
standing_cool = []


# 图片地址
pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
img = re.findall(pattern, date, re.S)
url = []
title = []
for i in img:
    url.append(i[1] or i[4])
    title.append(i[2] or i[5])
print(len(url), len(title))


# 作品类型
pattern = r'<p class="card-info-type" title="(.+?)">'
types_of_works = re.findall(pattern, date, re.S)
# print(types_of_works)
print(len(types_of_works))

# 人气数
pattern = r'<span class="statistics-view" title="共(.+?)人气">'
popularity = re.findall(pattern, date, re.S)
# print(popularity)
popularity.insert(4, '无')
popularity.insert(39, '无')

# 点赞数
pattern = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
number_of_likes = re.findall(pattern, date, re.S)

number_of_likes.insert(4, '无')
number_of_likes.insert(39, '无')
print(len(number_of_likes))

# 评论数
pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
comment = re.findall(pattern, date, re.S)
# print(comment)
comment.insert(4, '无')
comment.insert(39, '无')
print(len(comment))


# 作者名字
pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
author_name = re.findall(pattern, date, re.S)
print(len(author_name))
authorResult = []
count = 0
for i in author_name:
    count += 1
    author = i[1] or i[3]
    authorResult.append(author)

for i in range(len(comment)):
    work_information = {}
    work_information = {'图片地址': url[i], '作品名字': title[i], '作品类型': types_of_works[i], '人气数': popularity[i], '点赞数': number_of_likes[i], '评论数': comment[i], '作者名': authorResult[i]}
    standing_cool.append(work_information)
print(standing_cool, len(standing_cool))
import csv
header = ['图片地址', '作品名字', '作品类型', '人气数', '点赞数', '评论数', '作者名']
with open('作品信息.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 创建表格的写入者
    huo = csv.DictWriter(file, header)
    # 写入表头
    huo.writeheader()
    # 写入数据
    # 写入一条数据(字典)
    # csv_file.writerow({'姓名': '张三','性别': '男','年龄': 20,'身高': 180})
    # 写入多条数据(列表: 里面有多个字典)
    huo.writerows(standing_cool)