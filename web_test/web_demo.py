from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import select
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
element = driver.find_element_by_id("kw")
element.send_keys("selenium")
driver.find_element_by_id("su").click()
loc = driver.find_element_by_xpath("//a[text()=\" automates browsers. That's it!\"]").click()
print(loc)
# expected_conditions.visibility_of_element_located
# expected_conditions.

wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
base_handle = driver.current_window_handle
all_handles = driver.window_handles
for handle in all_handles:
    if handle != base_handle:
        driver.switch_to.window(handle)
driver.switch_to.default_content()
driver.switch_to.parent_frame()
# print(element.text)
driver.switch_to.alert
# print(element.tag_name)
sleep(10)
driver.quit()


# xpath定位
# 窗口切换
