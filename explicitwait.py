import time
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
# driver.implicitly_wait(8)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()

# WebDriverWait()     >>until>>expected condition>>check condition funtion(3)
obj=WebDriverWait(driver,10)
obj.until(expected_conditions.presence_of_element_located(('xpath',"//input[@name='username']"))).send_keys('Admin')
# driver.find_element('xpath',"//input[@name='username']").send_keys('Admin')
driver.find_element('xpath',"//input[@name='password']").send_keys('admin123')
driver.find_element('xpath',"//button[text()=' Login ']").click()
# button=obj.until(expected_conditions.presence_of_element_located(('xpath',"//button[text()=' Login ']")))
# button.click()
# driver.find_element('xpath', "//input[@placeholder='Search']").click()
obj.until(expected_conditions.presence_of_element_located(('xpath', "//input[@placeholder='Search']"))).click()
time.sleep(3)