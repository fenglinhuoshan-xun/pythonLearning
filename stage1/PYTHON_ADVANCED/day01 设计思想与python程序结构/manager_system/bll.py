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