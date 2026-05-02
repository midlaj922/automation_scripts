import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/frames?sublist=0')
driver.maximize_window()

frame =driver.find_element('xpath','//iframe[@class ="w-full h-96"]')
driver.switch_to.frame(frame)#it is used to switch to a specific frame it should have the reference to the frame which to be inspected

driver.find_element("id",'username').send_keys('John wick')
driver.find_element("id",'password').send_keys('jhon123')
driver.find_element("id",'submitButton').click()

time.sleep(5)

