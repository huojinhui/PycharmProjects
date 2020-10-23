import time


def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)


start = time.time()
print(f(40))
end = time.time()
dur = end - start
print(dur)