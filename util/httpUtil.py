import requests
from common.Consts import CommonData
import json

class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers = {"Content-Type":"application/json;charset=UTF-8"}

    def post(self,path,data):
        host = CommonData.host
        data_json = json.dumps(data)
        response = self.http.post(
            url = host+path,
            data = data_json,
            headers = self.headers
        )
        assert response.status_code == 200
        response_json = response.text
        response_dict = json.loads(response_json)
        return response_dict

    def get(self,path):
        host = CommonData.host
        response = self.http.get(
            url=host+path
        )
        assert response.status_code == 200
        response_json = response.text
        response_dict = json.loads(response_json)
        return response_dict

    # 打印http响应消息的函数
    def printresponse(self,response):
        print("\n------------HTTP response *begin--------------")
        print(response.status_code)
        for k, v in response.headers.items():
            print(f'{k},{v}')
        print("  ")
        print(response.content.decode("utf8"))
        print("\n------------HTTP response *end--------------")