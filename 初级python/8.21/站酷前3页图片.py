import requests, csv, re, lxml.etree
date = ''
count = 0
for j in range(1, 4):
    website = 'https://www.zcool.com.cn/?p=%s' %(j)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    response = requests.get(website, headers=headers)
    date += response.text
conten = lxml.etree.HTML(date)
conten_one = conten.xpath('//div[@class="card-box"]')
for i in conten_one:
    picture_address = i.xpath('.//div/a/img/@src')[0]
    count += 1
    print(count)
    url = picture_address
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    index = url.rfind('/')
    if index != -1:
        name = 'image' + url[index:]
    with open(name, 'wb') as file:
        file.write(response.content)