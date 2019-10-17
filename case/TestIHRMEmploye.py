import unittest

import requests

from day07接口测试人力资源管理系统.api.EmpAPI import EmpCRUD


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    def tearDown(self):
        self.session.close()
    def test_emp_add(self):
        response=self.emp_obj.add(self.session,'hgayfdy123','18656789012',542244)
        # 2.断言业务
        print("新增成功响应结果:", response.json())
    def test_emp_update(self):
        # 请求业务
        response = self.emp_obj.update(self.session,
                                       "1184404023436201984",
                                       "huluwa0803AAA")
        # 断言业务
        print("修改后的响应体:", response.json())
        self.assertEqual(True, response.json().get("success"))

        # 测试函数3: 查
    def test_emp_get(self):
        # 1.请求业务
        response = self.emp_obj.get(self.session, "1184404023436201984")
        # 2.断言
        print("查询到的用户信息:", response.json())
        self.assertEqual(10000, response.json().get("code"))

        # 测试函数4: 删

    def test_emp_delete(self):
        # app.my_log_config()
        # try:
            response = self.emp_obj.delete(self.session, "1184404023436201984")
            print("删除的响应结果:", response.json())
            self.assertIn("操作成功", response.json().get("message"))
        # except Exception as e:
        #     logging.info(e)