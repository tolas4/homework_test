import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# cases表格路径
excel_dir = os.path.join(base_dir, "Data/homework_cases.xlsx")

# 日志logger路径
logger_dir = os.path.join(base_dir, "Outputs/debuger.log")

# 配置文件option路径
option_dir = os.path.join(base_dir, "Data/option.ini")

# 测试用例地址
cases_dir = os.path.join(base_dir, "TestCases")

# 测试报告的路径
reports_dir = os.path.join(base_dir, "Outputs/reports")