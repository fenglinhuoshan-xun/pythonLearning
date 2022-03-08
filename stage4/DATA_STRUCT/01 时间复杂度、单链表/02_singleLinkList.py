"""
    python实现单链表
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """单链表类"""

    def __init__(self):
        """初始化一个空链表"""
        self.head = None  # 头节点为None的时候，为空链表

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None  # 链表为空时，返回True，不为空时，返回False

    def add(self, item):
        """在链表的头部添加一个节点"""
        # 注意：我们现在封装方法，封装完了之后，是要给用户或者自己用的，所有说，
        # 当我们真的要在链表的头部添加一个节点的时候，给用户留的接口一定要是个数据，数据区的元素，而不是节点，自己要在方法里实例出节点对象
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """在链表的尾部添加一个节点"""
        # cur为游标，从头节点开始依次往后移动至尾节点
        node = Node(item)
        # 空链表的情况
        if not self.head:
            self.head = node
            return
        cur = self.head  # 头节点
        while cur.next:
            cur = cur.next
        # 当次循环结束时，cur指向的是尾节点的位置
        cur.next = node
        node.next = None

    def length(self):
        """获取链表长度"""
        if not self.head:
            return 0
        count = 1
        cur = self.head
        while cur.next:
            cur = cur.next
            count += 1
        return count

    def insert(self, position, item):
        """在指定位置上添加节点，position从0开始"""
        node = Node(item)
        # 空链表的情况
        if not self.head or position > self.length() - 1:
            pre = self.append(node)
            return
        # 非空链表的情况
        pre = self.head
        middle = 0
        # 此处要写position - 1，因为pre要移动到前一个
        while middle < (position - 1):  # 移动到要插入位置的前一个位置
            pre = pre.next
            middle += 1
        node.next = pre.next
        pre.next = node

    def remove(self, item):
        """删除节点"""
        pre = None
        cur = self.head
        # 1. 删除头节点的情况
        if self.head.value == item:
            self.head = self.head.next
            return
            # 当cur为None时，即表示单链表中没有要删除的元素时，循环就结束了，即空链表没有问题
        # 2. 删除非头节点的情况
        while cur:
            if cur.value == item:
                pre.next = cur.next
                return
                # 移动两个游标
            pre = cur
            cur = cur.next

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        print()


if __name__ == '__main__':
    s = SingleLinkList()  # 空链表
    # 创建链表：100 --> 200 --> 300
    s.append(100)
    s.append(200)
    s.append(300)
    # 终端1：输出False
    print(s.is_empty())
    # 链表：10 --> 100 --> 200 --> 300
    # 终端2：10 100 200 300
    s.add(10)
    s.travel()
    # 终端3：4
    print(s.length())
    # 终端4：10 100 800 200 300
    s.insert(2, 800)
    s.travel()
    # 终端5：10 800 200 300
    s.remove(100)
    s.travel()
