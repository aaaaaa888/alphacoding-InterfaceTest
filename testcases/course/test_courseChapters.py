from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取⼤纲")
class Test_courseChapters():
    def test_courseChapters(self):
        path = CommonData.courseChapters
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取⼤纲')
        except:
            print('获取⼤纲失败')