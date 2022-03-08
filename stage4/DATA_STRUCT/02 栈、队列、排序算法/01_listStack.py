"""
顺序表存储的方式实现栈模型
思路：
    1. LIFO 后进先出
    2. 设计
        栈顶：列表的尾部作为栈顶，负责入栈和出栈操作
        栈底：列表的头部作为栈底，不负责任何操作
"""


class ListStack:
    def __init__(self):
        # 初始化一个空栈
        self.elems = []

    def is_empty(self):
        """判断栈是否为空，为空返回True，非空返回False"""
        return self.elems == []

    def push(self, item):
        """入栈：相当于在列表的尾部添加一个元素"""
        self.elems.append(item)

    def destack(self):
        """出栈：相当于在列表的尾部弹出一个元素"""
        if self.is_empty():
            raise Exception('destack from an empty stack')
        return self.elems.pop()

    def peek(self):
        """查看栈顶的元素：相当于查看列表的最后一个元素"""
        if self.is_empty():
            raise Exception('stack is empty')
        return self.elems[-1]

    def size(self):
        """栈大小：相当于获取元素中列表的数量"""
        return len(self.elems)


if __name__ == '__main__':
    s = ListStack()
    # 入栈操作：100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1：False
    print(s.is_empty())
    # 终端2：300
    print(s.destack())
    # 终端3：200
    print(s.destack())
    # 终端4：100
    print(s.peek())
    # 终端5：1
    print(s.size())
