from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


driver = webdriver.Chrome()

# 封装找元素
def find_ele(driver, path):
    return driver.find_element(By.XPATH, path)

# 窗口最大化
driver.maximize_window()

# 设置等待
wait = WebDriverWait(driver, 10)

# 一键登录url
url = "http://ats.weizhipin.com/wapi/zpats/super/login/to"
driver.get(url)

# 一键登录
phone = "14000015461"
log_phone = find_ele(driver, '//input[@name="account"]')
log_phone.send_keys(phone)
log_btn = find_ele(driver, '//input[@value="登录"]')
log_btn.click()

# 设置显性等待用于调试
sleep(5)
driver.quit()





