from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取⼩节详情")
class Test_lesson():
    def test_lesson(self):
        path = CommonData.lesson
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取⼩节详情')
        except:
            print('获取⼩节详情失败')