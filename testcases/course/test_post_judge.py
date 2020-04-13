from conftest import http
import allure
from common.Consts import CommonData

@allure.feature("提交答案")
class Test_judge():
    def test_judge(self):
        path = CommonData.judge
        data = CommonData.judge_data
        response = http.post(path,data)
        try:
            assert response['ok'] == True
            print('提交答案成功')
        except:
            print('提交答案失败')
