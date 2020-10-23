from typing import List

from aaa import ghj


# 冒泡排序
def bubble_sort(num):
    for i in range(len(num) - 1):
        flag = 1
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                flag = 2
        if flag == 1:
            break
        print(f"第{i + 1}次排序", num)
    return num


def bubble_sort2(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
        print(f"第{i + 1}次排序", num)
    return num


# 选择排序
def select_sort(num):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    return num


def select_sort2(num):
    for i in range(len(num) - 1):
        small = i
        for j in range(i + 1, len(num)):
            if num[small] > num[j]:
                small = j
        num[small], num[i] = num[i], num[small]
        print(f"第{i + 1}轮排序", num)
    return num


# 插入排序
def insert_sort(num: List[int]):
    if len(num) < 2:
        return num
    for right in range(1, len(num)):
        target = num[right]
        for left in range(right):
            if num[left] > target:
                num[left + 1:right + 1] = num[left: right]
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
    # 创建一个虚拟节点
    dummy = Node(0)
    # 指定新旧俩个链表的头
    pre = dummy
    current = head
    # 遍历旧链表的每一个节点
    while current is not None:
        temp = current.next
        # 对新链表进行遍历找到合适的位置插入从旧链表取出的节点
        while pre.next is not None and pre.next.data < current.data:
            pre = pre.next
        # 此节点指向后面
        current.next = pre.next
        # 然后pre指向此节点
        pre.next = current
        # current变成下一个节点, pre又回到头结点
        current = temp
        pre = dummy
    # 返回新链表的头结点
    return dummy.next


def output(head: Node):
    string = ""
    while head:
        string += f"{head}" + "-->"
        head = head.next
    return string + "end"


# 归并排序
def merge_sort(num: List[int]):
    if len(num) <= 1:
        return num
    mid = len(num) >> 1
    left = num[0:mid]
    right = num[mid:]
    return pointer(merge_sort(left), merge_sort(right))


def merge(left, right):
    arr = []
    while left and right:
        if left[0] > right[0]:
            arr.append(right.pop(0))
        else:
            arr.append(left.pop(0))
    if left:
        arr.extend(left)
    if right:
        arr.extend(right)
    return arr


# 利用指针合并
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


# 快速排序
def quicksort(list1, start, end):
    if start >= end:
        return
    mid = partition1(list1, start, end)
    quicksort(list1, start, mid - 1)
    quicksort(list1, mid + 1, end)
    return list1


def partition(list1, start, end):
    pivot = list1[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and list1[p] <= pivot:
            p += 1
        while p <= q and list1[q] >= pivot:
            q -= 1
        if p < q:
            swap(list1, p, q)
    swap(list1, start, q)
    return q


# 单指针遍历
def partition1(list1, start, end):
    piovt = list1[start]
    slow = start
    for fast in range(start + 1, end + 1):
        if list1[fast] < piovt:
            slow += 1
            list1[fast], list1[slow] = list1[slow], list1[fast]
    list1[start] = list1[slow]
    list1[slow] = piovt
    return slow


def swap(list1, p, q):
    list1[p], list1[q] = list1[q], list1[p]


# 特别优秀的快排代码
def quicksort1(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort1(less) + [pivot] + quicksort1(greater)


# 计数排序
def count_sort(nums):
    new = [0 for i in range(max(nums) + 1)]
    print(new)
    for j in nums:
        new[j] += 1
    print(new)
    arr = []
    for k in range(max(nums) + 1):
        if new[k] == 0:
            continue
        for m in range(new[k]):
            arr.append(k)
    return arr


# 桶排序
def bucket_sort(nums: List):
    max_value = max(nums)
    min_value = min(nums)
    d = max_value - min_value

    bucket = [[] for i in range(len(nums))]

    for i in range(len(nums)):
        num = int((nums[i] - min_value) * (len(nums) - 1) / d)
        bucket[num].append(nums[i])

    for i in range(len(bucket)):
        bucket[i].sort()

    sort_arr = []
    for sub in bucket:
        for item in sub:
            sort_arr.append(item)

    return sort_arr


a = [0.5, 2.5, 3.2, 2.8, 4.5]
print(bucket_sort(a))












# a = [0, 2, 5, 4, 8, 6, 4, 8, 4, 6, 10]
# print(count_sort(a))

# a = bubble_sort([5, 4, 1, 2, 3])
# print("最终结果", a)
# a = bubble_sort2([5, 4, 1, 2, 3])
# print("最终结果", a)
# a = quicksort([5, 4, 1, 2, 3, 8, 12, 11, 10, 9, 7, 7], 0, 11)
# print("最终结果", a)


# if __name__ == '__main__':
#     s1 = Node(7)
#     s2 = Node(9)
#     s3 = Node(5)
#     s4 = Node(4)
#     s5 = Node(3)
#     s6 = Node(2)
#
#     s7 = Node(100)
#     s1.next = s2
#     s2.next = s3
#     s3.next = s4
#     s4.next = s5
#     s5.next = s6
#     s6.next = s7
#
#     print(output(insert_sort_list(s1)))


