import requests
a = 'https://www.baidu.com/s?wd=哈哈哈'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
}
rue = requests.get(a, headers=headers)
print(rue.text)
import lxml