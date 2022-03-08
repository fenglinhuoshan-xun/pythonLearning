"""
链式存储实现栈
思路：
    1. 栈特点：LIFO 后进先出
    2. 设计
        栈顶：链表头部作为栈顶，进行入栈和出栈操作
        栈底：链表尾部作为栈底，不进行任何操作
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListStack:
    def __init__(self):
        """初始化一个空栈"""
        self.head = None

    def is_empty(self):
        """判断栈是否为空"""
        return self.head == None

    def push(self, item):
        """入栈：相当于在链表的头部添加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        """出栈：相当于删除链表的头节点"""
        if self.is_empty():
            # 空链表的情况
            raise Exception('pop from an empty stack')
        item = self.head.value
        self.head = self.head.next
        return item

    def peek(self):
        """查看栈顶元素：相当于查看链表头节点的数据"""
        if self.is_empty():
            raise Exception("stack is empty")

        return self.head.value

    def size(self):
        """栈大小；相当于查看链表中节点的数量"""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    s = LinkListStack()
    # 入栈操作：100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1：False
    print(s.is_empty())
    # 终端2：300
    print(s.pop())
    # 终端3：200
    print(s.peek())
    # 终端4：2
    print(s.size())
