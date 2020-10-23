import re, requests,time
from lxml import etree
url = 'http://category.dangdang.com/pg5-cp01.03.56.00.00.00.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Cookie': 'from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.Ks0000KjAT1xjWiuTLQDLNDtyCb1ouaWOf8GEJwDqSAxdJDzOUsaSKaSC58W5tTLAOgzHxy3y%7C%230-%7C-; __permanent_id=20200825120019303314498480430126163; __ddc_15d_f=1598328019%7C!%7C_utm_brand_id%3D11106; ddscreen=2; __visit_id=20200825222310654364406156636635533; __out_refer=1598365391%7C!%7Cwww.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593%25E7%25BD%2591; __ddc_1d=1598365391%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1598365391%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1598365391%7C!%7C_utm_brand_id%3D11106; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; __rpm=mix_104643.850439%2C6411.1.1598365408825%7Cs_605253.451684912835%2C451684912836..1598365424263; search_passback=50c9eea7bcbe8946281f455f00000000; __trace_id=20200825222441750858077172417103554; pos_9_end=1598365482658; pos_6_start=1598365482882; pos_6_end=1598365482974; ad_ids=3029482%2C2756405%2C2756384%2C3271083%2C3057046%2C2923816%7C%232%2C2%2C1%2C3%2C3%2C1'
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
print(new_book_id, len(new_book_id))