from typing import List


def bubble_sort(randlist):
    for i in range(len(randlist) - 1):
        flag = 1
        for j in range(len(randlist) - 1 - i):
            if randlist[j] > randlist[j + 1]:
                randlist[j], randlist[j + 1] = randlist[j + 1], randlist[j]
                flag = 2
        if flag == 1:
            break
    return randlist


def select_sort(randlist):
    for i in range(len(randlist) - 1):
        small = i
        for j in range(i + 1, len(randlist)):
            if randlist[i] > randlist[j]:
                small = j
        randlist[i], randlist[small] = randlist[small], randlist[i]
        return randlist


def insert_sort(num: List[int]):
    if len(num) < 2:
        return num
    for right in range(1, len(num)):
        target = num[right]
        for left in range(right):
            if num[left] > target:
                num[left + 1:right + 1] = num[left:right]
                num[left] = target
                break
        print(f"第{right}轮排序", num)
    return num


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node{self.data}"


def insert_sort_list(head: Node):
    dummy = Node(0)
    current = head
    pre = dummy
    while current is not None:
        temp = current.next
        while pre.next is not None and pre.next.data < current.data:
            pre = pre.next
        current.next = pre.next
        pre.next = current
        pre = dummy
        current = temp
    return dummy.next


def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) >> 1
    left = num[0:mid]
    right = num[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    arr = []
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))
    while left:
        arr.append(left.pop(0))
    while right:
        arr.append(right.pop(0))
    return arr


def pointer(left, right):
    arr = []
    left_point = 0
    right_point = 0
    while left_point < len(left) and right_point < len(right):
        if left[left_point] > right[right_point]:
            arr.append(right[right_point])
            right_point += 1
        else:
            arr.append(left[left_point])
            left_point += 1
    arr.extend(right[right_point:])
    arr.extend(left[left_point:])
    return arr


def quick_sort(list, start, end):
    if start >= end:
        return
    mid = partition(list, start, end)
    quick_sort(list, start, mid - 1)
    quick_sort(list, mid + 1, end)


def swap(list, p, q):
    list[p], list[q] = list[q], list[p]


def partition(list, start, end):
    povit = list[0]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and p < povit:
            p += 1
        while p <= q and q > povit:
            q += 1
        swap(list, p, q)
    swap(list, start, q)
    return q


def count_sort(nums):
    new = [0 for i in range(max(nums) + 1)]
    for k in nums:
        new[k] += 1
    arr = []
    for k in range(max(nums) + 1):
        if new[k] == 0:
            continue
        else:
            for m in range(new[k]):
                arr.append(k)
    return arr