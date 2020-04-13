from conftest import http
from common.Consts import CommonData
import allure

@allure.feature("登录模块")
class Test_login:
    @allure.story("登录成功")
    def test_login_success(self):
        path = "/api/auth/login"
        data = {'loginId':CommonData.username,
                'password':CommonData.password,
                'orgId':CommonData.orgId}
        response = http.post(path,data)
        print(response)
        assert response['ok'] == True
        #logger.info('登录成功')

    @allure.story("用户不存在")
    def test_login_fail1(self):
        path = "/api/auth/login"
        data = {'username': 'aaaaaa',
                'password': CommonData.password,
                'orgId':CommonData.orgId}
        response = http.post(path, data)
        assert response['ok'] == False
        #logger.info('用户不存在')

    @allure.story("用户名不能为空")
    def test_login_fail2(self):
        path = "/api/auth/login"
        data = {'username': '',
                'password': CommonData.password,
                'orgId':CommonData.orgId}
        response = http.post(path, data)
        assert response['ok'] == False
        #logger.info('用户名不能为空')

    @allure.story("用户名或密码错误")
    def test_login_fail3(self):
        path = "/api/auth/login"
        data = {'username': CommonData.username,
                'password': 'aaa',
                'orgId':CommonData.orgId}
        response = http.post(path, data)
        assert response['ok'] == False
        #logger.info('用户名或密码错误')


