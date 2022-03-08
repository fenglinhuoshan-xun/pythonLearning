from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
        学生管理视图：主要负责界面逻辑
    """

    def __init__(self):
        self.__controller = StudentManagerController()

    def __display_menu(self):  # 做成私有的，因为别的地方也不需要去调用它，只需要在这个类内部自己使用
        print("1）添加学生信息")
        print("2）显示学生信息")
        print("3）删除学生信息")
        print("4）修改学生信息")
        print("5）根据成绩升序排列")

    def __select_menu(self):  # 做成私有的
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_students_order_by_score()

    def main(self):  # 为了让别人调用方便
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        name = input("请输入学生的姓名：")
        score = self.__input_integer("请输入学生的成绩：")
        age = self.__input_integer("请输入学生年龄：")
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __input_integer(self, message):
        while True:
            try:
                return int(input(message))
            except:
                print("输入有误")

    def __output_students(self):
        for item in self.__controller.stu_list:
            print("学生编号是：%d 姓名是：%s 年龄是：%d 成绩是%d." % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        # stu_id = int(input("请输入要删除的编号："))
        stu_id = self.__input_integer("请输入要删除的编号：")
        if self.__controller.remove_stuent(stu_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        # id = int(input("请输入需要修改的学生编号："))
        # name = int(input("请输入需要修改的学生姓名："))
        # age = int(input("请输入需要修改的学生年龄："))
        # score = int(input("请输入需要修改的学生成绩："))
        # stu = StudentModel(name,age,score,id)

        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生编号："))
        stu.id = self.__input_integer("请输入需要修改的学生编号：")
        stu.name = input("请输入需要修改的学生姓名：")
        # stu.age = int(input("请输入需要修改的学生年龄："))
        stu.age = self.__input_integer("请输入需要修改的学生年龄：")
        # stu.score = int(input("请输入需要修改的学生成绩："))
        stu.score = self.__input_integer("请输入需要修改的学生成绩：")
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_students_order_by_score(self):
        self.__controller.order_by_score()
        self.__output_students()
