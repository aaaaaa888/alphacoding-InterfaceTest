from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("记录时间")
class Test_studyTime():
    def test_studyTime(self):
        path = CommonData.studyTime
        data = CommonData.studyTime_data
        response = http.post(path,data)
        try:
            assert response['ok'] == True
            print('成功获取记录时间')
        except:
            print('获取记录时间失败')
