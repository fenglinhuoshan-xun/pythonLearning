"""
    创建员工管理器：
        1. 记录所有员工
        2. 计算总薪资
    岗位:
        1. 程序员：底薪 + 项目分红
        2. 测试员：底薪 + Bug数 * 5
        ...
    要求：
        增加新员工，管理器代码不变
    体会：三大特征，四大原则
"""


class EmployeeManager:
    def __init__(self):
        self.__emplyees = []

    def add_employee(self, emp):
        self.__emplyees.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        for item in self.__emplyees:
            total_salary += item.get_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary=0):  # 把共性往爹的身上提
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary


# -------------------------
class Programmer(Employee):
    def __init__(self, base_salary=0, bonus=0):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        # return self.base_salary + self.bonus
        return super().get_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary=0, bug_count=0):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_salary(self):
        return super().get_salary() + self.bug_count


manager = EmployeeManager()
manager.add_employee(Programmer(10000, 500000))
manager.add_employee(Tester(8000, 200))
print(manager.calculate_total_salary())
