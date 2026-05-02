import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/frames/multiple?sublist=2')
driver.maximize_window()

outerframe1=driver.find_element('xpath','//iframe[@class="w-full h-96"][1]')
driver.switch_to.frame(outerframe1)#it is used to switch to a specific frame it should have the reference to the frame which to be inspected

driver.find_element("id",'email').send_keys('Admin@gmail.com')
driver.find_element("id",'password').send_keys('Admin@1234')
driver.find_element("id",'confirm-password').send_keys('Admin@1234')
driver.find_element("id",'submitButton').click()

time.sleep(5)
driver.switch_to.default_content()
outerframe2=driver.find_element('xpath','//div[@class="w-1/2"][2]/iframe')
driver.switch_to.frame(outerframe2)#it is used to switch to a specific frame it should have the reference to the frame which to be inspected

driver.find_element("id",'username').send_keys('SuperAdmin@gmail.com')
driver.find_element("id",'password').send_keys('SuperAdmin@1234')
driver.find_element("id",'submitButton').click()
time.sleep(2)
driver.switch_to.default_content()

driver.find_element("xpath",'//a[text()="Nested with Multiple iframe"]').click()
time.sleep(5)

