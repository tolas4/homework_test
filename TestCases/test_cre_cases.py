import unittest
from Common.func_requests import send_request
from Common.func_rep_data import EnvData, clear_EnvData, req_data_by_re
from Common.func_getuser import get_username, get_email, new_password, get_proname, get_interfacesname
from Common.func_excel import Get_excel
from ddt import ddt, data
from Common.func_extract_data import extract_data_from_res
from Common.func_address import excel_dir
from jsonpath import jsonpath
from Common.func_logger import logger

sh = Get_excel(excel_dir, "创建用例")
cases = sh.read_all_datas()


@ddt
class TextCreateCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("*********用例开始**************")
        clear_EnvData()
        setattr(EnvData, "username", get_username())
        setattr(EnvData, "email", get_email())
        setattr(EnvData, "password", new_password())
        setattr(EnvData, "pro_name", get_proname())
        setattr(EnvData, "in_name", get_interfacesname())
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        logger.info("********单个用例结束*******")
        pass
    #
    # def tearDownClass(cls) -> None:
    #     pass

    @data(*cases)
    def test_create_cases(self, case):
        request_data = req_data_by_re(case["request_data"])
        if hasattr(EnvData, "token"):
            response = send_request(case["method"], case["url"], request_data, token=EnvData.token)
        else:
            response = send_request(case["method"], case["url"], request_data)
        if case["extract_data"]:
            extract_data_from_res(case["extract_data"], response)
        self.assertEqual(response.status_code, case["expected"])
