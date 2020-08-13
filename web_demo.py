from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu,com")
element = driver.find_element_by_id("kw")
print(element.text)
print(element.tag_name)
driver.quit()