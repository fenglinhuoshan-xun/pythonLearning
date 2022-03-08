"""
二叉排序树转为排序的双向链表
思路：
    1. 中序遍历，拿到排序的序列
    2. 调整left和right的属性值
        情况1：头节点特殊
        情况2：中间节点操作
        情况3：尾节点特殊
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def tree_to_linklist(self, root):
        # 1. 中序遍历：[<node 1 at xxx>,<node 2 at xxx>,<node 3 at xxx>,...]
        li = self.mid_travel(root)
        # 情况1：空树情况
        if len(li) == 0:
            return None
        if len(li) == 1:
            return root  # 本身只有一个树根，就可以说它也是个双向链表
        # 2. 搞定头尾节点
        li[0].left = None
        li[0].right = li[1]
        li[-1].right = None
        li[-1].left = li[-2]

        # 3. 搞定中间节点
        for i in range(1, len(li) - 1):
            li[i].left = li[i - 1]
            li[i].right = li[i + 1]

        # 返回双向链表的头节点，就能找到这个链表
        return li[0]

    def mid_travel(self, root):
        if not root:
            return
        self.mid_travel(root.left)
        self.result.append(root)
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
    head = s.tree_to_linklist(n12)
    # 遍历这个双向链表
    cur = head
    while cur:
        print(cur.value, end=' ')
        cur = cur.right
