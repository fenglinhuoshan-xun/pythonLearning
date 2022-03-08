"""
游戏核心逻辑控制器
"""
import random

from model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    # 1. 定义函数，将list_merge中的零元素移动到末尾
    def __zero_to_end(self):
        """
            零元素移动到末尾
            思路：从后往前依次判断，如果是零元素，则删除后追加零
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 2. 定义函数，将list_merge中的元素进行合并（相邻且相同）
    def __merge(self):
        """
            合并
            思路：
                将零元素后移
                判断如果相邻且相同则合并
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    # 3. 定义函数，将二维列表map中的元素向左移动
    def move_left(self):
        """
            向左移动
            思路：将每行（一维列表）赋值给全局变量list_merge
                 再通过merge函数操作数据
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    # 4. 定义函数，将二维列表map中的元素向右移动
    def move_right(self):
        """
            向右移动
            思路：将每行（反向切片）赋值给全局变量list_merge
                 再通过merge函数操作数据
                 再对list_merge（反向切片）
        """
        for line in self.__map:
            # 因为切片，所以创建了新列表
            self.__list_merge = line[::-1]
            self.__merge()  # 操作的是新列表
            line[::-1] = self.__list_merge

    def __square_matrix_tranpose(self):
        for c in range(len(self.__map) - 1):
            for r in range(c + 1, len(self.__map)):
                self.__map[r][c], self.__map[c][r] = self.__map[c][r], self.__map[r][c]

    # 5. 定义函数，将二维列表map中的元素向上移动
    def move_up(self):
        """
            思想：方阵转置
                 调用向左移动
                 方阵转置
        """
        self.__square_matrix_tranpose()
        self.move_left()
        self.__square_matrix_tranpose()

    # 6. 定义函数，将二维列表map中的元素向下移动
    def move_down(self):
        """
            思想：方针转置
                 调用向右移动
                 方阵转置
        """
        self.__square_matrix_tranpose()
        self.move_right()
        self.__square_matrix_tranpose()

    def generate_new_number(self):
        # 选择位置
        # 计算所有空位置
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0: return
        # 再随机选择一个
        loc = random.choice(self.__list_empty_location)  # 从集合中取元素
        # 计算数字
        # self.map[loc[0]][loc[1]] = self.__select_random_number()
        self.map[loc.r][loc.c] = self.__select_random_number()

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()  # 清空
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    # self.__list_empty_location.append((r, c))
                    self.__list_empty_location.append(LocationModel(r, c))

    def is_game_over(self):
        # 判断是否有空位置
        if len(self.__list_empty_location) > 0:
            return False

        for r in range(len(self.map)):
            for c in range(len(self.map[r]) - 1):
                if self.map[r][c] == self.map[r][c + 1] or self.map[c][r] == self.map[c + 1][r]:  # 判断横向是否可以移动
                    return False

        # for r in range(len(self.map)):
        #     for c in range(len(self.map[r]) - 1):
        #         if self.map[r][c] == self.map[r][c + 1]:  # 判断横向是否可以移动
        #             return False
        #
        # for c in range(len(self.map)):
        #     for r in range(len(self.map) - 1):
        #         if self.map[r][c] == self.map[r][c]:  # 判断竖向向是否可以移动
        #             return False
        return True


if __name__ == '__main__':
    controller = GameCoreController()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.move_down()
    print(controller.map)
