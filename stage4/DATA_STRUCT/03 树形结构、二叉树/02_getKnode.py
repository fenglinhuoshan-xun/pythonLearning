"""
给定一颗二叉搜索树，找到其中第K小的节点
思路：
    1. 先对二叉搜索树进行中序遍历，拿到递增的序列
    2. 利用列表的下标索引取出对应的值
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def get_k_node(self, root, k):
        # 中序遍历，得到递增的序列
        li = self.mid_travel(root)
        # print(li)
        if k <= 0 or k > len(li):
            raise Exception('Index out of range')

        return li[k - 1]

    def mid_travel(self, root):
        """中序遍历，返回值为递增的序列"""
        if not root:
            return

        self.mid_travel(root.left)
        self.result.append(root.value)
        self.mid_travel(root.right)

        return self.result


if __name__ == '__main__':
    s = Solution()
    n12 = Node(12)
    n5 = Node(5)
    n2 = Node(2)
    n9 = Node(9)
    n15 = Node(15)
    n16 = Node(16)
    n17 = Node(17)
    n18 = Node(18)
    n19 = Node(19)
    # 创建二叉排序树
    n12.left = n5
    n12.right = n18
    n5.left = n2
    n5.right = n9
    n18.left = n15
    n18.right = n19
    n15.right = n17
    n17.left = n16
    # 测试方法
    # print(s.get_k_node(n12, 1).value)
    print(s.get_k_node(n12, 1))
    print(s.get_k_node(n12, 20))
