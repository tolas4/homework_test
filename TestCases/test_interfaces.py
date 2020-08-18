import unittest
from Common.func_requests import send_request
from Common.func_rep_data import EnvData, clear_EnvData, req_data_by_re
from Common.func_getuser import get_username, get_email, new_password, get_proname, get_interfacesname
from Common.func_excel import Get_excel
from ddt import ddt, data
from Common.func_address import excel_dir
from jsonpath import jsonpath
from Common.func_logger import logger


sh = Get_excel(excel_dir, "创建接口")
cases = sh.read_all_datas()

@ddt
class TestInterfaces(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        clear_EnvData()
        logger.info("********创建项目用例的前置*********")
        username = get_username()
        email = get_email()
        pwd = new_password()
        resp_register = send_request("POST", "/user/register/", {"username": username, "email":email, "password":pwd, "password_confirm":pwd})
        setattr(EnvData, "token", (jsonpath(resp_register.json(), "$..token"))[0])
        setattr(EnvData, "name", get_proname())
        resp_pro = send_request("POST", "projects/", {"name": EnvData.name, "leader": "可优","tester": "某人", "programmer": "某人", "publish_app": "XXX应用", "desc": "xxxx描述"}, token=EnvData.token)
        setattr(EnvData, "pro_id", str((jsonpath(resp_pro.json(), "$..id"))[0]))

    @data(*cases)
    def test_interfaces(self, case):
        setattr(EnvData, "in_name", get_interfacesname())
        request_data = req_data_by_re(case["request_data"])
        response = send_request(case["method"], case["url"], request_data, token=EnvData.token)
        print(response.text)