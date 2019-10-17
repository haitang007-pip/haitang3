import unittest


# 组织测试套件
from HTMLTestRunner import HTMLTestRunner

from case.TestIHRMUser import TestUser
from case.TestIHRMEmploye import TestEmployee

suite=unittest.TestSuite()
suite.addTest(TestUser('test_login_success'))
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))
# 执行套件对象
with open("./report/report.html","wb") as f:
    runner = HTMLTestRunner(f,title="我的测试报告",description="版本 v1.0")
    runner.run(suite)