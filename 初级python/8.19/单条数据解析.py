import csv, re
with open('站酷.html', 'r', encoding='utf - 8') as file:
    date = file.read()
pattern = r'<div class="card-box">(.+?)</div>\s+</div>'
date_one = re.findall(pattern, date, re.S)
standing_cool = []
for i in date_one:
    # 地址和图片名
    pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
    img = re.findall(pattern, i, re.S)
    url = []
    title = []
    url.append(img[0][1] or img[0][4])
    title.append(img[0][2] or img[0][5])
    print(title)
    print(url)
    # 作品类型
    pattern = r'<p class="card-info-type" title="(.+?)">'
    types_of_works = re.findall(pattern, i, re.S)
    # 人气数
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    popularity = re.findall(pattern, date, re.S)
    if len(popularity) > 0:
        popularity = popularity[0]
    else:
        popularity.append('无')
    print(popularity)
    # 点赞数
    pattern = r'<span class="statistics-view" title="共(.+?)人气">'
    fansResult = re.findall(pattern, i, re.S)
    # 说明有数据
    if len(fansResult) > 0:
        fansResult = fansResult[0]
    else:
        fansResult = '无'
    print(fansResult)
    # 评论数
    pattern = r'<span class="statistics-comment" title="共(.+?)评论">'
    comment = re.findall(pattern, i, re.S)
    if len(comment) > 0:
        comment = comment[0]
    else:
        comment.append('无')
    # 作者名
    pattern = r'(<span class="user-avatar showMemberCard">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(class="card-item">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="content_ad_publisher">)'
    author_name = re.findall(pattern, i, re.S)
    authorResult = []
    author = author_name[0][1] or author_name[0][3]
    authorResult.append(author)

    work_information = {}
    work_information = {'图片地址': url[0], '作品名字': title[0], '作品类型': types_of_works[0], '人气数': popularity,
                        '点赞数': fansResult, '评论数': comment, '作者名': authorResult[0]}
    standing_cool.append(work_information)


header = ['图片地址', '作品名字', '作品类型', '人气数', '点赞数', '评论数', '作者名']
with open('库.csv', 'w', encoding='utf-8-sig', newline='') as file:
    # 创建表格的写入者
    huo = csv.DictWriter(file, header)
    # 写入表头
    huo.writeheader()

    huo.writerows(standing_cool)