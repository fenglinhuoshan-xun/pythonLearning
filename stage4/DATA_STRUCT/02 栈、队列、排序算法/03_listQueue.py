"""
顺序存储方式实现队列模型
思路：
    1. 目标：队列 FIFO 先进先出
    2. 设计
        队头：列表的头部，出队操作(pop(0))
        队尾：列表的尾部，入队操作(append())
"""


class ListQueue:
    def __init__(self):
        """初始化一个空队列"""
        self.elems = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.elems == []

    def enqueue(self, item):
        """入队：相当于在里列表的尾部添加一个元素"""
        self.elems.append(item)

    def dequeue(self):
        """出队：相当于在列表的头部弹出一个元素"""
        if self.is_empty():
            raise Exception("dequeue from an empty queue")
        return self.elems.pop(0)

    def size(self):
        """返回队列的大小：相当于获取列表的长度"""
        return len(self.elems)


if __name__ == '__main__':
    q = ListQueue()
    # 入队： 100 200 300
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 终端1：False
    print(q.is_empty())
    # 终端2：100
    print(q.dequeue())
    # 终端3：200
    print(q.dequeue())
    # 终端4：1
    print(q.size())
