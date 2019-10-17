import json
import unittest

import requests
from parameterized import parameterized

from day07接口测试人力资源管理系统 import app
from day07接口测试人力资源管理系统.api.UserApi import Userlogin


def read_json():
    data=[]
    with open(app.PRO_PATH + '/data/login_data.json','r',encoding='utf-8')as f:
        for value in json.load(f).values():
            mobile=value.get('mobile')
            password=value.get('password')
            success=value.get('success')
            code=value.get('code')
            message=value.get('message')
            ele=(mobile, password, success, code, message)
            data.append(ele)
    return data

class TestUser(unittest.TestCase):
    def setUp(self):
        self.session=requests.Session()
        self.user_obj = Userlogin()
    def tearDown(self):
        self.session.close()
    @parameterized.expand(read_json())
    def test_login(self,mobile, password, success, code, message):
        response=self.user_obj.login(self.session,mobile, password)
        result=response.json()
        self.assertEqual(success,result.get('success'))
        self.assertEqual(code,result.get('code'))
        self.assertIn(message,result.get('message'))
    def test_login_success(self):
        response=self.user_obj.login(self.session,'13800000002','123456')
        result=response.json()
        print('登陆成功的响应结果',result)
        self.assertEqual(True, result.get('success'))
        self.assertEqual(10000, result.get('code'))
        self.assertIn('操作成功', result.get('message'))
        # 提取token值
        token=result.get('data')
        print('登陆成功后的token值',token)
        app.TOKEN=token #变局部变量为全局变量