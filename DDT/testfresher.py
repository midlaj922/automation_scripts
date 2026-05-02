import time

from selenium.webdriver import Keys

import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"https://testfreshers.qspiders.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)

path=r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\TestfreshDDT.xlsx'
rows=Utilities.rows_count(path,"Sheet1")

for i in range(2,rows+1):
    UN=Utilities.read_data(path,"Sheet1",i,1)
    PW=Utilities.read_data(path,"Sheet1",i,2)
    time.sleep(3)



    user=driver.find_element('id', 'standard-adornment-weight')
    user.send_keys(Keys.CONTROL+"a")
    user.send_keys(Keys.DELETE)



    driver.find_element('id','standard-adornment-weight').send_keys(UN)

    time.sleep(3)
    pas=driver.find_element('id', 'password')
    pas.send_keys(Keys.CONTROL+"a")
    pas.send_keys(Keys.DELETE)


    driver.find_element('id','password').send_keys(PW)
    time.sleep(3)
    driver.find_element('xpath', '//button[text()="Sign In"]').click()
    time.sleep(5)
    if driver.title=="TestFreshers | Home":
        print("Test Passed")
        Utilities.write_data(path,"Sheet1",i,4,"pass")
        driver.find_element('xpath', '//ul[@id="_navLinksStudents_md4v8_1"]/li[6]').click()
        time.sleep(5)
        driver.find_element('xpath', '//p[text()="Logout"]').click()
        time.sleep(2)
        driver.find_element('xpath', '//button[text()="Yes"]').click()
        time.sleep(5)
    else:
        print("Test Failed")
        Utilities.write_data(path,"Sheet1",i,4,"fail")
        time.sleep(2)

