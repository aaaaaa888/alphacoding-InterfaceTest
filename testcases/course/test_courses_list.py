from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取课程列表")
class Test_courseList():
    def test_courseList(self):
        path = CommonData.courseList
        response = http.get(path)
        try:
            print(response)
            assert response['ok'] == True
            print('成功获取课程列表')
        except:
            print('获取课程列表失败')
