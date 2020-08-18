from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.baidu,com")
element = driver.find_element_by_id("kw")


# expected_conditions.visibility_of_element_located
# expected_conditions.

wait = WebDriverWait(driver, 20)
us = wait(f)
print(element.text)
print(element.tag_name)
driver.quit()


# xpath定位
