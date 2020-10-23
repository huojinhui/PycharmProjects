import requests, os
def download_skin(url, name1):
    url = 'https://game.gtimg.cn/images/lol/act/img/skin/big1008.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    name1 = 'aaa'
    if not os.path.exists(name1):
        # 创建文件夹
        os.mkdir(name1)
        index = url.rfind('/')
        if index != -1:
            name = name1 + url[index:]
        with open(name, 'wb') as file:
            file.write(response.content)


url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
response = requests.get(url, headers=headers)
id_list = []
id = response.json()['hero']
for i in id:
    id_list.append(i['heroId'])
print(id_list)