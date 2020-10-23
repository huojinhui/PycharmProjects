import re
# a = ',mAa1232wabcWwqew1232qewewqew21331weer'
# # result = re.search('[1]', a)
# # result = re.search('[0-9]', a)
# # result = re.search('[a-z]', a,)
# # result = re.search('[A-Z]', a)
# result = re.search('[A-Z]', a)
# print(result)

a = input('请输入一个手机号:')
pattern = r'^1[3456]\d{9}$'
result = re.search(pattern, a)
if result == None:
    print('不是手机号')
else:
    print('是手机号')
b = input('请输入一个座机号')
resule = re.search(r'^(0\d[2,3]-)?\d{7}$', b)
if resule == None:
    print('不是')
else:
    print('是')
