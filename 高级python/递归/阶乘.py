# 求n的阶乘
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 有n个台阶,青蛙每次跳一节或俩节,有多少种跳法.
def f(n):
    if n == 1 or n == 2:
        return n
    else:
        return f(n - 1) + f(n - 2)


print(f(5))
