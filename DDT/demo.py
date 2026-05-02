import time
import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"https://testfreshers.qspiders.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element('id', 'standard-adornment-weight').send_keys("7736919809")

time.sleep(2)
driver.find_element('id', 'password').send_keys("Mid@Qspider2002")
time.sleep(2)
driver.find_element('xpath', '//button[text()="Sign In"]').click()
time.sleep(8)
# ___________________
driver.find_element('xpath', '//ul[@id="_navLinksStudents_md4v8_1"]/li[6]').click()
time.sleep(5)
driver.find_element('xpath','//p[text()="Logout"]').click()
time.sleep(2)
driver.find_element('xpath','//button[text()="Yes"]').click()
time.sleep(5)