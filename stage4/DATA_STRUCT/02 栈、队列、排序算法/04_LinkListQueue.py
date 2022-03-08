"""
链式存储方式实现队列
思路：
    1. 队列：FIFO
    2. 设计
        入队：相当于在链表尾部添加一个节点
        出队：相当于删除链表头节点
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListQueue:
    """初始化一个空队列"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断是否为空队列：相当于判断链表头节点是否为None"""
        return self.head == None

    def enqueue(self, item):
        """入队：相当于在链表的尾部添加一个节点"""
        node = Node(item)
        # 1. 空链表的情况
        if self.is_empty():
            self.head = node
            return
        # 2. 非空链表的情况
        cur = self.head
        while cur.next:
            cur = cur.next  # 循环结束，cur指向尾节点
        cur.next = node
        node.next = None

    def dequeue(self):
        """出队：相当于删除链表的头节点"""
        # 1. 空链表的情况
        if self.is_empty():
            raise Exception('dequeue from an empty queue')
        # 2. 非空链表的情况
        item = self.head.value
        self.head = self.head.next
        return item

    def size(self):
        """队列大小：相当于计算链表中有多少个节点"""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    s = LinkListQueue()
    # 入队：100 200 300
    s.enqueue(100)
    s.enqueue(200)
    s.enqueue(300)
    # 终端1：False
    print(s.is_empty())
    # 终端2：100
    print(s.dequeue())
    # 终端3:2
    print(s.size())
