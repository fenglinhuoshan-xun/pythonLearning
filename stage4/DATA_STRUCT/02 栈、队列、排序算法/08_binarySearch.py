"""
python实现二分查找（折半查找）
"""


def binary_search(li, item):
    """二分查找"""
    # first：起始
    first = 0
    last = len(li) - 1

    while first <= last:
        # 一轮比较
        mid = (first + last) // 2
        if li[mid] < item:
            first = mid + 1
        elif li[mid] > item:
            last = mid - 1
        else:
            return True  # 查找的元素存在

    return False


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if binary_search(li, 8):
        print('ok')
    else:
        print('no')
