from day07接口测试人力资源管理系统 import app


class Userlogin:
    def login(self,session,mobile,password):

        return session.post(app.BASE_UEL+'login',
                            json={"mobile":mobile,"password":password})