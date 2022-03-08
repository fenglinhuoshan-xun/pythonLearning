"""
    异常处理
"""


def div_apple(apple_count):
    person_count = int(input("请输入人数："))  # ValueError
    result = apple_count / person_count  # ZeroDivisionError
    print("每个人分%d个苹果" % result)


# 写法1：根据不同的错误，做出不同的逻辑处理
# 官方建议的写法，分门别类
# try:
#     div_apple(10)
# except ValueError:
#     print("输入的必须是整数")
# except ZeroDivisionError:
#     print("输入的不能是零")

# 写法2：不同的错误，相同的处理逻辑
# 官方不建议，但开发时常用
# try:
#     div_apple(10)
# # except Exception: # Exception是所有异常的基类
# except:  # 甚至可以不用写Exception
#     print("出错喽")

# 写法3：如果没有出错，可以单独定义逻辑
# try:
#     div_apple(10)
# except:
#     print("出错喽")
# else:
#     print("没有错误")

# 写法4：
try:
    div_apple(10)
finally:  # 无论是否有错，都会执行
    print("无论是否错误，一定执行的逻辑")
