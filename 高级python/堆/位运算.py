a = int('000000001011', 2)
count = 0
while a != 0:
    a = a & (a - 1)
    count += 1
    print(count)
print(count)


def singleNumber(nums):
    res = 0
    for i in nums:
        res = res ^ i
    return
