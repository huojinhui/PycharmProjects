import time


# 穷举法
def common_divisor1(a, b):
    if a > b:
        for i in range(b, 0, -1):
            if (a % i) == 0 and (b % i) == 0:
                return i
    elif b > a:
        for i in range(a, 0, -1):
            if (a % i) == 0 and (b % i) == 0:
                return i


# 优化
def common_divisor4(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        for i in range(b // 2, 1, -1):
            if (a % i) == 0 and (b % i) == 0:
                return i


# 辗转相除法
def common_divisor2(a, b):
    if b > a:
        a, b = b, a
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b
    if b == 1:
        return None
    return b


# 优化
def common_divisor5(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return common_divisor5(b, a % b)


# 根相减损法
def common_divisor3(a, b):
    if b > a:
        a, b = b, a
    if a % 2 == 0 and b % 2 == 0:
        count = 0
        while a % 2 == 0 and b % 2 == 0:
            a = a / 2
            b = b / 2
            count += 1
        while b != a - b:
            difference = a - b
            if difference > b:
                difference, b = b, difference
            a = b
            b = difference
        if b == 1:
            return 1
        return b * (2 ** count)
    else:
        while b != a - b:
            difference = a - b
            if difference > b:
                difference, b = b, difference
            a = b
            b = difference
        if b == 1:
            return 1
        return b


# 优化
def get_greatest_common_divisor(a, b):
    if a - b == 0:
        return a
    big = max(a, b)
    small = min(a, b)
    return get_greatest_common_divisor(big - small, small)


print(common_divisor3(24, 12))

