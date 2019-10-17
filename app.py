import os

BASE_UEL='http://182.92.81.159/api/sys/'
# 动态获取路径方法1
# PRO_PATH=os.getcwd()
# print('项目绝对路径',PRO_PATH)

# 方法2
# FILE_ABS_PATH=os.path.abspath(__file__) #文件的绝对路径
# PRO_PATH=os.path.dirname(FILE_ABS_PATH)#项目的绝对路径
PRO_PATH=os.path.dirname(os.path.abspath(__file__))
TOKEN=None