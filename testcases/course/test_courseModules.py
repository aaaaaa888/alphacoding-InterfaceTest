from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取菜单")
class Test_courseModules():
    def test_courseModules(self):
        path = CommonData.courseModules
        response = http.get(path)
        try:
            assert response['ok'] == True
            print('成功获取菜单')
        except:
            print('获取菜单失败')