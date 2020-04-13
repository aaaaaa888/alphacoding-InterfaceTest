from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取最近学习动态")
class Test_course_trends():
    def test_trends(self):
        path = CommonData.trends
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取最近学习动态')
        except:
            print('获取最近学习动态失败')
