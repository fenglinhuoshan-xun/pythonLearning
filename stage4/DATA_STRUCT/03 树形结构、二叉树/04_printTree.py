"""
从上到下按层打印二叉树，同一层结点从左至右输出，每一层输出一行
思路：
    1. 队列思想FIFO（append() + pop(0)）
    2. 两个队列，存储当前层节点和下一层的节点
    3. 当前层操作完成后，可以和下一层交换变量
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree(self, root):
        # 1. 空树情况
        if not root:
            return
            # 2. 非空树情况
        cur_queue = [root]
        next_queue = []
        while cur_queue:
            cur_node = cur_queue.pop(0)
            print(cur_node.value, end=' ')
            # 添加这个节点的左右孩子到下一层的队列
            if cur_node.left:
                next_queue.append(cur_node.left)
            if cur_node.right:
                next_queue.append(cur_node.right)

            # 交换变量（交换当前层和下一层的变量）
            if not cur_queue:
                cur_queue, next_queue = next_queue, cur_queue
                print()


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
