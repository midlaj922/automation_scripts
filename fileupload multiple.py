import time

import onefile
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

var=driver.find_element('id','multipleFilesInput')
path=(r"C:\Users\MD. MIDELAJ\Downloads\MUHAMMED-MIDLAJ-FlowCV-Resume-20260128 (2).pdf",r"C:\Users\MD. MIDELAJ\Downloads\Scania_NG_Addon_Pack.scs")
for i in path:
    var.send_keys(i)
time.sleep(2)






