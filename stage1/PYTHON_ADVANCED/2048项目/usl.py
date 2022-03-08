"""
    游戏界面逻辑模块
"""
import os

from bll import GameCoreController


class GameConsoleView:
    """
        控制台界面类
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__controller.generate_new_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("游戏结束")

    def __move_map_for_input(self):
        dir = input("请输入方向：")
        if dir == 'w':
            self.__controller.move_up()
        elif dir == 's':
            self.__controller.move_down()
        elif dir == 'a':
            self.__controller.move_left()
        elif dir == 'd':
            self.__controller.move_right()

    def main(self):
        self.__start()
        self.__update()

    def __draw_map(self):
        os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item, end='\t')
            print()
