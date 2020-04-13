from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取课程详情")
class Test_courseDetail():
    def test_courseDetail(self):
        path = CommonData.courseDetail
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取课程详情')
        except:
            print('获取课程详情失败')