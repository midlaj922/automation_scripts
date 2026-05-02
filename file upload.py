import time

import onefile
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

var=driver.find_element('id','singleFileInput')
path=(r"C:\Users\MD. MIDELAJ\Downloads\MUHAMMED-MIDLAJ-FlowCV-Resume-20260128 (2).pdf")
var.send_keys(path)
time.sleep(2)






