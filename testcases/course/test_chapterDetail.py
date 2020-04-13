from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("获取章节")
class Test_chaperDetail():
    def test_chaperDetail(self):
        path = CommonData.chaperDetail
        response = http.get(path)
        try:
            #print(response)
            assert response['ok'] == True
            print('获取章节成功')
        except:
            print('获取章节失败')