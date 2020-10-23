import re
with open('站酷.html', 'r', encoding='utf-8') as file:
    content = file.read()

# 规则
# 图片url地址
# pattern = '''target="_blank" z-st="home_main_card_cover">
#             <img src="(.+?)"
#                  srcset=".+?"
#                  title="(.+?)" alt="">'''
# 38条
# pattern = r'target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">'
# 2条
# pattern = r'z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">'

# 保证数据的顺序不变
pattern = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
# 从源代码里面取图片url地址
# 返回值: 列表
result = re.findall(pattern, content, re.S)
print(len(result))
count = 0
# 取出数据
for i in result:
    count += 1
    print(count)
    # print(i[1],i[2])
    # print(i[4],i[5])
    # 当第1条-第4条没有值的时候
    url = i[1] or i[4]
    title = i[2] or i[5]
    print(url, title)
    # print(i)
