"""
    场景:
        1.测试购物车接口，需要提前使用手机验证码登录
        2.关注点是购物车接口，而手机验证码登录实现繁琐
        3.需要简化登录，比如:输入任意手机验证码都可以登录成功
"""
import unittest


# 登录功能(开发编写的)
def login(tel, code):
    # ..... 业务实现
    return False


# 购物车功能
def cart():
    print("显示购物车信息")


# 测试
class TestShop(unittest.TestCase):
    def test_cart(self):
        # 前置条件:先登录
        flag = login("13012345678", "6666")

        # 确保登录成功,再测试购物车
        if flag:
            cart()
        else:
            print("登录失败")

