#!/usr/bin/python
#coding=UTF-8
import unittest
from Common.func_address import reports_dir, cases_dir
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    s = unittest.TestLoader().discover(cases_dir)
    br = BeautifulReport(s)
    br.report("家庭作业自动化测试", "report.html", reports_dir)