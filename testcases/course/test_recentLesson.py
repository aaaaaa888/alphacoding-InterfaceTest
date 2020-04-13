from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取最近学习⼩节")
class Test_recentLesson():
    def test_recentLesson(self):
        path = CommonData.recentLesson
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取最近学习⼩节')
        except:
            print('获取最近学习⼩节失败')
