import unittest

from Common.func_excel import Get_excel
from Common.func_address import excel_dir
from Common.func_logger import logger
from ddt import ddt, data
from Common.func_getuser import get_email, get_username, new_password
from Common.func_rep_data import EnvData, req_data_by_re, clear_EnvData
from Common.func_requests import send_request
from Common.func_db import ConnDB


sh = Get_excel(excel_dir, "注册")
cases = sh.read_all_datas()


@ddt
class TestRegister(unittest.TestCase):
    def setUp(self) -> None:
        clear_EnvData()
        logger.info("******注册用例的前置*******")
        setattr(EnvData, "username", get_username())
        setattr(EnvData, "email", get_email())
        setattr(EnvData, "password", new_password())

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("******注册用例的后置*******")

    @data(*cases)
    def test_register(self, case):
        if case["check_sql"]:
            db = ConnDB()
            _data = db.select_one(case["check_sql"])
            for key, value in _data.items():
                setattr(EnvData, key, value)
            db.close_db()
        request_data = eval(req_data_by_re(case["request_data"]))
        response = send_request(case["method"], case["url"], data=request_data)
        # resp = response.json()
        self.assertEqual(response.status_code, case["expected_code"])