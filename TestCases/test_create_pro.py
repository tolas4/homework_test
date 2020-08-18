import unittest
from Common.func_requests import send_request
from Common.func_rep_data import EnvData, clear_EnvData, req_data_by_re
from Common.func_getuser import get_username, get_email, new_password, get_proname
from Common.func_excel import Get_excel
from ddt import ddt, data
from Common.func_address import excel_dir
from jsonpath import jsonpath
from Common.func_logger import logger

sh = Get_excel(excel_dir, "创建项目")
cases = sh.read_all_datas()

@ddt
class TestCreatePro(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        logger.info("********创建项目用例的前置*********")
        username = get_username()
        email = get_email()
        pwd = new_password()
        resp = send_request("POST", "/user/register/", {"username": username, "email":email, "password":pwd, "password_confirm":pwd})
        setattr(EnvData, "token", (jsonpath(resp.json(), "$..token"))[0])


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("*******创建项目用例的后置**********")
        pass


    @data(*cases)
    def test_create_pro(self, case):
        setattr(EnvData, "name", get_proname())
        request_data = req_data_by_re(case["request_data"])
        response = send_request(case["method"], case["url"], request_data, token=EnvData.token)
        self.assertEqual(response.status_code, case["expected"])

