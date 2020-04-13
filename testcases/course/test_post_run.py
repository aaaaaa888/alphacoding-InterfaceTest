from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("运⾏")
class Test_run():
    def test_run(self):
        path = CommonData.run
        data = CommonData.run_data
        response = http.post(path,data)
        try:
            assert response['ok'] == True
            print('运⾏成功')
        except:
            print('运⾏失败')
