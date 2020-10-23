import requests, re, os
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%86%8A%E7%8C%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%86%8A%E7%8C%AB&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=120&rn=30&gsm=78&1597993017616='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url, headers=headers)
counts = response.json()
print(counts)
count = 0
a = counts['data'][:len(counts['data']) - 1]
for img in a:
    count += 1
    # print(count, '++++')
    # 所有图片的url地址
    # print(img['hoverURL'])
    b = img['hoverURL']

    url = b
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    response = requests.get(url, headers=headers)
    # 文件的返回数据: 二进制数据
    # print(response.content)
    # 图片的名字
    # 获取最后一个/出现的位置
    index = url.rfind('/')
    dirName = 'image'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    if index != -1:
        name = 'images' + url[index:]
    #  images/xx.png
    # 下载: 二进制数据保存到本地
    if index != -1:
        name = dirName + url[index:]
    with open(name, 'wb') as file:
        file.write(response.content)
