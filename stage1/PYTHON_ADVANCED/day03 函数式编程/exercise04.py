"""
    在不改变原有功能的定义与调用情况下(进入后台、删除订单),
    为其增加新功能(验证权限).
"""


# 在python中，装饰器不是这样写的，这只是一个推倒的原理
def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("删除权限")
        return func(*args, **kwargs)

    return wrapper


@verify_permissions
def enter_background():
    print("进入后台")


@verify_permissions
def delete_order():
    print("删除订单")


# enter_background = verify_permissions + enter_background
# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

enter_background()
delete_order()
