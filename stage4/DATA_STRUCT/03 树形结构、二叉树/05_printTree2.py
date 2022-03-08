"""
之字形打印二叉树，奇数层从左至右打印，偶数层从右至左打印，一层打印一行
思路：
    1. 找思想LIFO：append() + pop()
    2. 奇数层：先添加right，再添加left
    3. 偶数层：先添加left，再添加right
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree(self, root):
        if not root:
            return
        # 非空树情况，栈思想（append()+pop()）
        cur_stack = [root]
        next_stack = []
        level = 1
        while cur_stack:
            cur_node = cur_stack.pop()
            print(cur_node.value, end=' ')
            # 奇数层：先左后右添加
            if level % 2 == 1:
                if cur_node.left:
                    next_stack.append(cur_node.left)
                if cur_node.right:
                    next_stack.append(cur_node.right)

            # 偶数层：先右后左添加
            else:
                if cur_node.right:
                    next_stack.append(cur_node.right)
                if cur_node.left:
                    next_stack.append(cur_node.left)
            # 交换变量
            if not cur_stack:
                cur_stack, next_stack = next_stack, cur_stack
                print()
                level += 1


if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p6 = Node(6)
    p7 = Node(7)
    p8 = Node(8)
    p9 = Node(9)
    p10 = Node(10)
    # 创建树
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    p4.left = p8
    p4.right = p9
    p5.left = p10
    s.print_tree(p1)
