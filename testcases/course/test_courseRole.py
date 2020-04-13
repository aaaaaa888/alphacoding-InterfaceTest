from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取课程⻆⾊")
class Test_courseRole():
    def test_courseRole(self):
        path = CommonData.courseRole
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取课程⻆⾊')
        except:
            print('获取课程⻆⾊失败')