"""
    步骤一：
        数据模型类：StudentModel
            数据：姓名 name，年龄 age，成绩 score，编号 id
        逻辑控制类：StudentManagerController
            数据：学生列表 __stu_list
            行为：获取列表 stu_list
                 添加学生 add_student
                 删除学生 remove_student(stu_id)
                 修改学生 update_student(new_stu)
                 根据成绩进行生序排列 order_by_score
    步骤二：
        界面视图类：StudentManagerView
            数据：逻辑控制对象__manager
            行为：
                显示菜单 __display_menu
                选择菜单项 __select_menu_item，入口逻辑 main
                输入学生 __input_students
                显示学生 __output_students
                删除学生信息 __delete_student
                修改学生信息 __modify_student
                根据成绩升序输出学生 __output_students_order_by_score
"""


class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器：主要核心业务逻辑处理，页面的逻辑它不管，所有不能出现input、print等内容
    """
    init_id = 1000  # 初始id，做成大家的，所有做成类变量

    @classmethod
    def __generate_id(cls, stu):  # 方法私有化，因为这个东西不需要我们的界面逻辑去访问，只需要添加学生的时候自己去用
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        # 数据是由类内部产生的，类内添加的，不来自于类外，即不需要由创建我的时候告诉我数据有哪些
        self.__stu_list = []  # 我的数据我做主，不由你来染指，做成只读属性

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加学生信息
        :param stu:需要添加的学生对象
        :return:
        """
        StudentManagerController.__generate_id(stu)
        self.__stu_list.append(stu)

    def remove_stuent(self, stu_id):
        """
            移除学生信息
        :param stu_id:需要移除的学生编号
        :return: 移除是否成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)  # 不能用del去删，想内存图
                return True  # 成功删除
        return False  # 删除失败

    def update_student(self, new_stu):
        """
            修改学生信息
        :param new_stu:需要修改的学生信息
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == new_stu.id:
                item.name = new_stu.name
                item.age = new_stu.age
                item.score = new_stu.score
                return True  # 修改成功
        return False  # 修改失败

    def order_by_score(self):
        """
            根据成绩生序排列
        :return:
        """

        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


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
        score = int(input("请输入学生的成绩："))
        age = int(input("请输入学生的年龄："))
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __output_students(self):
        for item in self.__controller.stu_list:
            print("学生编号是：%d 姓名是：%s 年龄是：%d 成绩是%d." % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        stu_id = int(input("请输入要删除的编号："))
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
        stu.id = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = int(input("请输入需要修改的学生年龄："))
        stu.score = int(input("请输入需要修改的学生成绩："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_students_order_by_score(self):
        self.__controller.order_by_score()
        self.__output_students()


view = StudentManagerView()
view.main()

# 测试
# controller = StudentManagerController()
# data01 = StudentModel("悟空", 23, 96)
# controller.add_student(data01)
# controller.add_student(StudentModel("八戒", 25, 65))
# print(controller.remove_stuent(1006))
# controller.update_student(StudentModel("孙悟空", 24, 97, 1000))
# controller.order_by_score()
# for item in controller.stu_list:
#     print(item.id, item.name)
