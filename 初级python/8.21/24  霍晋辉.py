import re, requests, os
from lxml import etree
# 1.下载英雄联盟英雄的皮肤图片: (要求每个英雄都有一个文件夹,文件夹是该英雄的名字,文件夹里面的图片文件就是这个英雄的皮肤)
# 取出英雄的序号
# url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# # 放英雄的id
# id_list = []
# # 取出英雄的id
# id = response.json()['hero']
# for i in id:
#     id_list.append(i['heroId'])
# # print(id_list)
# # 下载每一个英雄的皮肤图片并建立文件夹
# for j in id_list:
#     j = int(j)
#     # 请求每个英雄的数据
#     website = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(j)
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
#     }
#     # 放英雄的皮肤网址
#     skin_list = []
#     accept = requests.get(website, headers=header)
#     date = accept.json()
#     # 取出英雄的名字建立文件夹时命名用
#     hero_name = date['hero']['name']
#     # 取出英雄皮肤的网址
#     skin_website = date['skins']
#     for skin in skin_website:
#         # 有些网址为空,需要去除
#         if skin['mainImg'] != '':
#             skin_list.append(skin['mainImg'])
#     # 计数用
#     num = 0
#     # 下载每个英雄的皮肤
#     for i in skin_list:
#         url = i
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers)
#         # 判断有无文件夹,若无建立一个新的
#         name1 = hero_name
#         if not os.path.exists(name1):
#             # 创建文件夹
#             os.mkdir(name1)
#         # 取出/后面的元素, 对每个图片进行命名
#         index = url.rfind('/')
#         if index != -1:
#             name = name1 + url[index:]
#         # 将返回来的数据变成图片写入文件夹中
#         with open(name, 'wb') as file:
#             file.write(response.content)
#             num += 1
#             print(num)

# 2.下载简历模板: (站长素材)	http://sc.chinaz.com/jianli/free.html
# url = 'http://sc.chinaz.com/jianli/free_4.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
# }
# date0 = requests.get(url, headers=headers)
# # print(date.text)
# # with open('page.html', 'w', encoding='utf - 8') as file:
# #     file.write(date.text)
# with open('page.html', 'r', encoding='utf - 8') as file:
#     date1 = file.read()
# html = etree.HTML(date1)
# page_address = html.xpath('//div[@class="box col3 ws_block"]/a/@href')
# # print(page_address)
#
#
# # 取出下载地址
# num = 0
# for i in page_address:
#     url = i
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     with open('01.html', 'w', encoding='utf - 8') as file:
#         file.write(response.text)
#     with open('01.html', 'r', encoding='utf - 8') as file:
#         date = file.read()
#     html = etree.HTML(date)
#     result = html.xpath('//div[@class="clearfix mt20 downlist"]/ul[@class="clearfix"]/li/a/@href')
#     # print(result)
#     # print(response.text)
#     jianli = result[0]
#
#     # 下载简历压缩包
#     url = jianli
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     # print(response.content)
#     name = '{}.rar'.format(num)
#     with open(name, 'wb')as file:
#         file.write(response.content)
#     num += 1
#     print(num)


# 3.自己找一个图片网站(比如百度图片..),下载海量图片
#
# (按照自己在网页中的操作找出接口)

# 请求所有网页的数据
# userInput = input('请输入想下载的图片名称: ')
# # 计数
# count = 0
# for page in range(1, 5):
#     print('第{}页开始'.format(page))
#     url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=55&gsm=1e&1597988871073='
#     # 放get请求的参数
#     dic = {
#         'pn': 30 * page,
#         'rn': 30,
#         'queryWord': userInput,
#         'word': userInput
#     }
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
#     }
#     response = requests.get(url, headers=headers, params=dic)
#     content = response.json()
#     # 最后一个为空,所以用切片去掉最后一个
#     allData = content['data'][:len(content['data']) - 1]
#     # 取出所有图片的地址
#     for img in allData:
#         count += 1
#         imgUrl = img['hoverURL'] or img['middleURL']
#         print(count, '++++', imgUrl)
#         # 下载图片并保存到image文件夹
#         url = imgUrl
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
#         }
#         response = requests.get(url, headers=headers)
#         index = url.rfind('/')
#         if index != -1:
#             name = 'images' + url[index:]
#         with open(name, 'wb') as file:
#             file.write(response.content)
#     print('第{}页开始'.format(page))


# 4.自己实现一个翻译功能: http://www.iciba.com/
# (自己找接口,自己测试参数,自己测试请求头)板:
# url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
# headers = {
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'content-length': '130',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'cookie': 'BIDUPSID=090DCDD427C23ED46C73469BEBF3D5EC; PSTM=1598157327; BAIDUID=090DCDD427C23ED4C3F4A16733469EFA:FG=1; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1438_32619_32533_31254_32045_32117_32618_32583_32481; BCLID=8321505424183137430; BDSFRCVID=-uLOJeC62lQtFArr8VEWhFIx82KKnW7TH6ao7_xKfhlW5X1k2H1PEG0PDU8g0Ku-S2OOogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvtHJrwMDc2K4RH-xQ0KnLXKKOLV56aBp7keq8CD4vG5MKFKlKOLfQU2gcAXIP-Whv_SI32y5jHhT-m2-RhaP7UJG-DBKodtxJpsIJMQh_WbT8U5ecgJfR9aKviaKJEBMb1f66DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe4tX-NFJtj-jtx5; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1598160334; Hm_lpvt_246a5e7d3670cfba258184e42d902b31=1598160334; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1598160350; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=e31f9d230bc625e5922154dcb58bb6a9faa40f29_1598162278_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1598162294; __yjsv5_shitong=1.0_7_8f0392d4bb20a2dfaf20e14c8fa17278a9d4_300_1598162296109_114.249.27.54_dfd7e200',
#     'origin': 'https://fanyi.baidu.com',
#     'referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E9%AA%A8%E9%AA%BC&keyfrom=baidu&smartresult=dict&lang=auto2zh',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest'
# }
# dic = {
#     'query': '马'
# }
# response = requests.post(url, headers=headers, data=dic)
# print(response.json())
# with open('翻译.html', 'wb', encoding='utf - 8') as file:
#     file.write(response.json())


# 老师的优秀解法
# userInput = input('输入要翻译的内容: ')
# url = 'https://dict.iciba.com/dictionary/word/suggestion?nums=5&ck=709a0db45332167b0e2ce1868b84773e&timestamp=1598234096722&client=6&uid=123123&key=1000006&is_need_mean=1&signature=bd609d96e3fb89632b9bb062869f1a75'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
# }
# dic = {
#     'word': userInput
# }
# response = requests.get(url, headers=headers, params=dic)
# result = response.json()['message'][0]['means'][0]['means']
# # 转为字符串显示时好看
# result = ','.join(result)
# print(result)