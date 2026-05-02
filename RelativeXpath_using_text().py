import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
driver.find_element('xpath',"//input[@name='username']").send_keys('Admin')
driver.find_element('xpath',"//input[@name='password']").send_keys('admin123')
driver.find_element('xpath',"//button[text()=' Login ']").click()
driver.find_element('css selector',"placeholder#Search").click()