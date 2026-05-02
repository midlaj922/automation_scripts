import time
import Utilities
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r"https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()
path=r'C:\Users\MD. MIDELAJ\Desktop\SELENIUM\DDT\DDT.xlsx'
rows=Utilities.rows_count(path,"Sheet1")



for r in range(2,rows+1):
    UN=Utilities.read_data(path,"Sheet1",r,1)
    PWW=Utilities.read_data(path,"Sheet1",r,2)
    driver.find_element('id','username').clear()
    driver.find_element('id','username').send_keys(UN)
    time.sleep(1)
    driver.find_element('id','password').clear()
    driver.find_element('id','password').send_keys(PWW)
    time.sleep(1)
    driver.find_element('id','submit').click()




    if driver.current_url=="https://practicetestautomation.com/logged-in-successfully/":
        Utilities.write_data(path,"Sheet1",r,4,'Pass')
        driver.back()
        time.sleep(1)
        print("test Passed")
    else:
        Utilities.write_data(path,"Sheet1",r,4,'Fail')
        print("test Failed")