"""
python实现归并排序
思路：
    1. 先分
    2. 再合
    整体思路：递归思想
"""


# 1. 先分
def merge_sort(li):
    # 递归出口：当每个列表中只有一个元素时
    if len(li) == 1:
        print(li)
        return li  # 最里层的返回值
    # [6,5,3,8]
    # 1. 先分
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    # 递归思想，左右两个小列表需要继续拆分
    left_li = merge_sort(left)
    right_li = merge_sort(right)

    # 2. 合并
    return merge(left_li, right_li)


# 因为递推到最深层已经分完了，所以合，肯定是在回归的过程中合
# 2. 再合
def merge(left_li, right_li):
    """合并函数"""
    # [5,6] [3,8]
    result = []
    while len(left_li) > 0 and len(right_li) > 0:
        if left_li[0] >= right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))
    # 循环结束后，一定有一个列表为空
    if left_li:
        result.extend(left_li)
    if right_li:
        result.extend(right_li)

    return result  # 是两个列表合并后的列表


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(li))

    # print(merge_sort(li))  # 最外层的返回值 None
    # print(merge([5, 6], [3, 8]))  # [3, 5, 6, 8]
