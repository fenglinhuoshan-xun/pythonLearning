"""
python实现二叉树
经过分析后，每个节点应该有三个属性，分别为：数据区、左孩子、右孩子
"""


class Node:
    """二叉树的节点类"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """初始化一个空树（树根为None的树为空树）"""
        self.root = None

    def add(self, item):
        """在二叉树中添加一个节点"""
        node = Node(item)
        # 情况1：空树
        if not self.root:
            self.root = node
            return
            # 情况2：非空树的情况
        # 队列思想，从树根开始判断
        node_list = [self.root]
        while True:
            cur = node_list.pop(0)
            # 1. 判断左孩子是否存在
            if cur.left:
                node_list.append(cur.left)
            else:
                cur.left = node
                return  # 写return或者break都行
            # 2. 判断右孩子是否存在
            if cur.right:
                node_list.append(cur.right)
            else:
                cur.right = node
                return

    def breadth_travel(self):
        """二叉树广度遍历：从上到下，从左至右"""
        node_list = [self.root]
        while node_list:
            cur = node_list.pop(0)
            print(cur.value, end=' ')
            # 添加左孩子
            if cur.left:
                node_list.append(cur.left)
            # 添加右孩子
            if cur.right:
                node_list.append(cur.right)
        # 打印空行
        print()

    def pre_travel(self, root):
        """前序遍历：根左右"""
        if not root:
            return

        print(root.value, end=' ')  # print跟的是根
        self.pre_travel(root.left)
        self.pre_travel(root.right)

    def mid_travel(self, root):
        """中序遍历：左根右"""
        if not root:
            return
        self.mid_travel(root.left)
        print(root.value, end=' ')
        self.mid_travel(root.right)

    def rear_travel(self, root):
        """后序遍历：左右根"""
        if not root:
            return
        self.rear_travel(root.left)
        self.rear_travel(root.right)
        print(root.value, end=' ')


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    bt.add(10)
    # 终端1（广度遍历）：1 2 3 4 5 6 7 8 9 10
    bt.breadth_travel()
    # 终端2（前序遍历）
    bt.pre_travel(bt.root)
    print()
    # 终端3（中序遍历）
    bt.mid_travel(bt.root)
    print()
    # 终端4（后序遍历）
    bt.rear_travel(bt.root)
    print()
