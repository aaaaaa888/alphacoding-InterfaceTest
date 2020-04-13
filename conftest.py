from util.httpUtil import HttpUtil
from common.Consts import CommonData
import pytest
import os

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/report/"
LOG_DIR = BASE_DIR + "/logs/"

http = HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path = "/api/auth/login"
    data = {
        'loginId':CommonData.username,
        'password':CommonData.password,
        'orgId': CommonData.orgId
    }
    response = http.post(path,data)
    print('登录成功')