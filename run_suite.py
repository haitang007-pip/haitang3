import unittest


# 组织测试套件
from day07接口测试人力资源管理系统.case.TestIHRMUser import TestUser
from day07接口测试人力资源管理系统.case.TestIHRMEmploye import TestEmployee

suite=unittest.TestSuite()
suite.addTest(TestUser('test_login_success'))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))
# 执行套件对象
runner=unittest.TextTestRunner()
runner.run(suite)