import re, requests, csv, json, pymysql,time
from lxml import etree

num = 1500
for i in range(25, 31):
    alldate = []
    time.sleep(5)
    url = 'http://category.dangdang.com/pg{}-cp01.03.56.00.00.00.html'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Cookie': 'from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.Ks0000KjAT1xjWiuTLQDLNDtyCb1ouaWOf8GEJwDqSAxdJDzOUsaSKaSC58W5tTLAOgzHxy3y%7C%230-%7C-; __permanent_id=20200825120019303314498480430126163; __ddc_15d_f=1598328019%7C!%7C_utm_brand_id%3D11106; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __visit_id=20200826160917503139674682107473470; __out_refer=; __ddc_1d=1598429358%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1598429358%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1598429358%7C!%7C_utm_brand_id%3D11106; search_passback=4b12865044e24f1d541a465f00000000; pos_9_end=1598429783003; pos_6_end=1598429783279; ad_ids=3225951%2C3225890%2C3225806%2C3272544%2C3271083%2C2756405%2C2756384%7C%233%2C3%2C3%2C2%2C3%2C3%2C2; pos_6_start=1598430869616; __trace_id=20200826163432684766042965346995314; __rpm=s_605253.451684912835%2C451684912836..1598429753933%7Cs_605253.451684912835%2C451684912836..1598430872697'
    }
    response = requests.get(url, headers=headers)
    # with open('当当网.html', 'w', encoding='utf-8') as file:
    #     file.write(response.text)
    # print(response.text)
    html = etree.HTML(response.text)
    book_id = html.xpath('//ul[@class="bigimg"]/li/@id')
    new_book_id = []
    for i in book_id:
        new_book_id.append(i[1:])

    for j in new_book_id:
        time.sleep(0.5)
        url = 'http://product.dangdang.com/{}.html'.format(j)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Cookie': 'from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.Ks0000KjAT1xjWiuTLQDLNDtyCb1ouaWOf8GEJwDqSAxdJDzOUsaSKaSC58W5tTLAOgzHxy3y%7C%230-%7C-; __permanent_id=20200825120019303314498480430126163; __ddc_15d_f=1598328019%7C!%7C_utm_brand_id%3D11106; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __visit_id=20200826160917503139674682107473470; __out_refer=; __ddc_1d=1598429358%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1598429358%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1598429358%7C!%7C_utm_brand_id%3D11106; __rpm=mix_65152.403752%2C5357.1.1598429358566%7Cs_605253.451684912835%2C451684912836..1598429753933; search_passback=4b12865044e24f1d3a1a465f00000000; __trace_id=20200826161555300193369449180703449; pos_9_end=1598429755952; pos_6_end=1598429756091; ad_ids=3225951%2C3225890%2C3225806%2C3272544%2C3271083%2C2756405%2C2756384%7C%233%2C3%2C3%2C2%2C2%2C2%2C1; pos_6_start=1598429770089'
        }
        response = requests.get(url, headers=headers)
        response.encoding='gbk'
        with open('其中一本书的.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        # print(response.text)
        html = etree.HTML(response.text)
        title = html.xpath('//*[@id="product_info"]/div[1]/h1/@title')
        if len(title) == 0:
            title = '无'
        else:
            title = title[0]
        author = html.xpath('//*[@id="author"]/a[1]/text()')
        if len(author) == 0:
            author = '无'
        else:
            author = author[0]
        print(author)
        press = html.xpath('//*[@id="product_info"]/div[2]/span[2]/a/text()')
        if len(press) == 0:
            press = '无'
        else:
            press = press[0]
        publication_time = html.xpath('//*[@id="product_info"]/div[2]/span[3]/text()')
        if len(publication_time) == 0:
            publication_time = '无'
        else:
            publication_time = publication_time[0]
        comment = html.xpath('//*[@id="comm_num_down"]/text()')
        if len(comment) == 0:
            comment = '无'
        else:
            comment = comment[0]
        e_book = html.xpath('//*[@id="e-book-price"]/text()')
        # print(e_book)
        if len(e_book) == 0:
            e_book = '无'
        else:
            e_book = e_book[0]
        book = html.xpath('//*[@id="dd-price"]/text()')
        if len(book) == 0:
            book = '无'
        else:
            book = book[1]
        # print(book)
        dic = {
            '网址': url,
            '书名': title,
            '作者': author,
            '出版社': press,
            '出版时间': publication_time,
            '评论': comment,
            '电子书价格': e_book,
            '纸质版价格': book
        }
        alldate.append(dic)


        # csv数据持久化
        header = ['网址', '书名', '作者', '出版社', '出版时间', '评论', '电子书价格', '纸质版价格']
        with open('世界名著信息表.csv', 'a', encoding='utf-8-sig', newline='') as file:
            huo = csv.DictWriter(file, header)
            if num == 0:
                huo.writeheader()
            huo.writerow(dic)

        # 写入mysql
        db = pymysql.connect('localhost', 'root', '', '123')
        cursor = db.cursor()
        sql = "INSERT INTO message (url,title, author, press, publication, comment, e_book, book) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');"%(dic['网址'], dic['书名'], dic['作者'], dic['出版社'], dic['出版时间'], dic['评论'], dic['电子书价格'], dic['纸质版价格'])
        cursor.execute(sql)
        num += 1
        print(num)


    # json数据持久化
    # with open('站酷.json', 'r', encoding='utf-8') as file:
    #     dic = json.load(file)
    #     count = dic['count']
    #     alldata = dic['data']
    # b = {
    #     'date': alldate
    # }
    # with open('世界名著信息.json', 'w', encoding='utf-8') as file:
    #     json.dump(b, file, ensure_ascii=False, indent=4)