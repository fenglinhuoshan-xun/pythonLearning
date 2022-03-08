"""
python实现快速排序
思路：
    1. 找到基准值
    2. 左游标右移，遇到比基准值大的停
    3. 右游标左移，遇到比基准值小的停
    情况1：左游标<右游标（左右游标互换位置）
    情况2：左游标>右游标（右游标和基准值互换位置）
"""


def quick_sort(li, first, last):
    # 递归出口
    # 基准值的正确位置为0，splist_position = 0，就是说它左边没值了，即就是它自己就是最小的元素
    # first：0
    # last：split_position - 1
    if first > last:
        return

    # 找到基准值正确位置的下标索引
    split_position = part(li, first, last)
    # 递归思想，左右两边同时继续执行快排
    quick_sort(li, first, split_position - 1)
    quick_sort(li, split_position + 1, last)


def part(li, first, last):
    """给一个基准值找到正确位置"""
    # first：快速排序的那部分的基准值（第一个元素）的下标索引
    # last：快速排序的那部分的最后一个元素的下标索引
    mid = li[first]
    lcursor = first + 1
    rcursor = last
    sign = True
    while sign:
        # 左游标右移，遇到比基准值大的，停
        while lcursor <= rcursor and li[lcursor] <= mid:
            lcursor += 1
        # 右游标左移，遇到比基准值小的，停
        while lcursor <= rcursor and li[rcursor] >= mid:
            rcursor -= 1
        # 循环结束时，左右游标都停在一个位置，左游标有可能小于右游标，也有可能左游标大于右游标
        if lcursor < rcursor:
            # 左右游标互换位置
            li[lcursor], li[rcursor] = li[rcursor], li[lcursor]
        else:
            # 右游标和基准值互换位置
            li[first], li[rcursor] = li[rcursor], li[first]
            # 一旦执行到这个分支，基准值的正确位置已经找到，终止此循环
            sign = False
    # 返回了一个基准值的正确位置
    return rcursor


if __name__ == '__main__':
    li = [6, 5, 888, 3, 1, 8, 666, 7, 2, 4]
    quick_sort(li, 0, len(li) - 1)
    print(li)
