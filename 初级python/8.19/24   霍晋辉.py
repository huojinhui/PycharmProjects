# # 1.站酷: https://www.zcool.com.cn/
# # 把该网站的数据保存400条下来;格式和周五要求的格式一样
import urllib.request, re, csv
# # 1 准备网址
date = ''
for i in range(1, 11):
    url = 'https://www.zcool.com.cn/?p=%s#tab_anchor'%(i)
    # 2.请求头
    a = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    # 3.构建网络请求
    request = urllib.request.Request(url, headers=a)
    # 4响应对象
    response = urllib.request.urlopen(request)
    date += response.read().decode()
    with open('代码库.html', 'w', encoding='utf-8') as file:
        file.write(date)


with open('代码库.html', 'r', encoding='utf - 8') as file:
    date = file.read()
pattern = r'<div class="card-box">(.+?)</div>\s+</div>'
date_one = re.findall(pattern, date, re.S)
standing_cool = []
num = 0
for i in date_one:
    # 地址和图片名
    pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'

    img = re.findall(pattern, i, re.S)
    url = []
    title = []
    url.append(img[0][1] or img[0][4])
    title.append(img[0][2] or img[0][5])
    # print(title)
    # print(url)
    # 作品类型
    pattern = r'<p class="card-info-type" title="(.+?)">'
    types_of_works = re.findall(pattern, i, re.S)
    # 人气数
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    popularity = re.findall(pattern, date, re.S)
    if len(popularity) > 0:
        popularity = popularity[0]
    else:
        popularity = '无'
    # print(popularity)
    # 点赞数
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    fansResult = re.findall(pattern, i, re.S)
    # 说明有数据
    if len(fansResult) > 0:
        fansResult = fansResult[0]
    else:
        fansResult = '无'
    # print(fansResult)
    # 评论数
    pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
    comment = re.findall(pattern, i, re.S)
    if len(comment) > 0:
        comment = comment[0]
    else:
        comment = '无'
    # 作者名
    pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)|(<span class="user-avatar">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)'
    author_name = re.findall(pattern, i, re.S)
    authorResult = []
    print(author_name)

    author = author_name[0][1] or author_name[0][3] or author_name[0][5]
    authorResult.append(author)
    num += 1
    print(num)
    print(author)

    work_information = {}
    work_information = {'图片地址': url[0], '作品名字': title[0], '作品类型': types_of_works[0], '人气数': popularity,
                        '点赞数': fansResult, '评论数': comment, '作者名': authorResult[0]}
    standing_cool.append(work_information)


header = ['图片地址', '作品名字', '作品类型', '人气数', '点赞数', '评论数', '作者名']
with open('400条库.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 创建表格的写入者
    huo = csv.DictWriter(file, header)
    # 写入表头
    huo.writeheader()

    huo.writerows(standing_cool)
# 2.致设计: https://www.zhisheji.com/
# 保存该网页的第一页的数据,存入到csv

url = 'https://www.zhisheji.com/'
# 2.请求头
a = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
# 3.构建网络请求
request = urllib.request.Request(url, headers=a)
response = urllib.request.urlopen(request)
date = response.read().decode()
with open('致设计库.html', 'w', encoding='utf-8') as file:
    file.write(date)

with open('致设计库.html', 'r', encoding='utf-8') as file:
    date = file.read()
    print(date)
