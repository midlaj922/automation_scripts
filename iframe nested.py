import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/frames/nested?sublist=1')
driver.maximize_window()

outerframe=driver.find_element('xpath','//iframe[@class ="w-full h-96"]')
driver.switch_to.frame(outerframe)#it is used to switch to a specific frame it should have the reference to the frame which to be inspected
innerframe=driver.find_element('xpath',"//section[@class ='main_form_container']/div[2]/iframe")
driver.switch_to.frame(innerframe)
driver.find_element("id",'email').send_keys('Admin@gmail.com')
driver.find_element("id",'password').send_keys('Admin@1234')
driver.find_element("id",'confirm-password').send_keys('Admin@1234')
driver.find_element("id",'submitButton').click()
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element("xpath",'//a[text()="Multiple iframe"]').click()
time.sleep(5)

