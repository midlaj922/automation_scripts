import time

import onefile
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/fileUpload?sublist=0&scenario=1')
driver.maximize_window()

driver.find_element('id','fullName').send_keys('Jhon Wick')
driver.find_element('id','emailId').send_keys('jhonwick@gmail.com')
driver.find_element('id','password').send_keys('jhon@123')
driver.find_element('id','mobile').send_keys('7744112255')
dropdown=driver.find_element('id','city')
obj=Select(dropdown)
obj.select_by_visible_text('Bangalore')
time.sleep(2)
var=driver.find_element('id','resume')
path=(r"C:\Users\MD. MIDELAJ\Downloads\MUHAMMED-MIDLAJ-FlowCV-Resume-20260128 (2).pdf")
var.send_keys(path)
time.sleep(2)
button =driver.find_element('xpath','//button[@type="submit"]').click()
time.sleep(2)

