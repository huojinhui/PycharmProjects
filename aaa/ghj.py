import random


def randint1(n, big: int):
    a = []
    for i in range(n):
        b = random.randint(1, big)
        a.append(b)
    return a