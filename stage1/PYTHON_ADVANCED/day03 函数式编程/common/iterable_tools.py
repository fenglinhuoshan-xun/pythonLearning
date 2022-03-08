"""
    可迭代对象工具模块
"""


# 我们将通过的代码放在单独的模块中，以后的用的时候，直接复制粘贴即可


class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代对象中查找满足条件的所有元素
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_condition: 函数类型，查找的条件，核心逻辑
        :return: 生成器对象，推算出满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def first(iterable, func_condition):
        """
            在可迭代对象当中查找满足第一个条件的元素（单个）
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_condition: 函数类型，查找的条件，核心逻辑
        :return: 第一个满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable, func_condition):
        """
            在可迭代对象中，获取满足条件的元素数量
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_condition: 函数类型，查找的条件
        :return: int类型，数量
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def select(iterable, func_handle):
        """
            通用的筛选方法
        :param iterable: 可迭代对象类型，需要筛选的数据
        :param func_handle: 筛选的逻辑
        :return: 生成器对象
        """
        for item in iterable:
            yield func_handle(item)

    @staticmethod
    def is_exists(iterable, func_condition):
        """
            判断可迭代对象中是否存在某个条件的对象
        :param iterable: 可迭代对象类型，需要筛选的数据
        :param func_exists: 查找的条件
        :return: bool，True表示存在，False表示不存在
        """
        for item in iterable:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(iterable, func_condition):
        sum_value = 0
        for item in iterable:
            sum_value += func_condition(item)
        return sum_value

    # @staticmethod
    # def get_max(iterable,func01, func02):
    #     max_value = func01()
    #     for i in range(1, len(iterable)):
    #         if max_value < func02(i):
    #             max_value = func02(i)
    #     return max_value

    @staticmethod
    def get_max(iterable, func_condition):
        """
            根据条件在可迭代对象中获取最大元素
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_condition: 指定条件
        :return: 最大元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(max_value) < func_condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def delete_all(iterable, func_conditon):
        """
            根据条件删除多个元素
        :param iterable: 可迭代对象类型，需要删除的数据
        :param func_conditon: 删除条件
        :return: 删除的元素数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if func_conditon(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def order_by(iterable, func_condition):
        """
            根据条件升序排列
        :param iterable: 可迭代对象类型，需要排序的数据
        :param func_condition: 比较的条件
        :return: 无
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func_condition(iterable[r]) > func_condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
