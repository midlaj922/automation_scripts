import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3')
driver.maximize_window()

outerframe1=driver.find_element('xpath','//iframe[@class="w-full h-96"]')
driver.switch_to.frame(outerframe1)#it is used to switch to a specific frame it should have the reference to the frame which to be inspected
innerframe=driver.find_element('xpath','//section[@class="main_form_container"]/div[2]/iframe')
driver.switch_to.frame(innerframe)


email=driver.find_element('xpath','//div[@class="form-group"][1]/iframe')
driver.switch_to.frame(email)
driver.find_element("id",'email').send_keys('Admin@gmail.com')
driver.switch_to.parent_frame()


password=driver.find_element('xpath','//div[@class="form-group"][2]/iframe')
driver.switch_to.frame(password)
driver.find_element("id",'password').send_keys('Admin@1234')
driver.switch_to.parent_frame()

confirm=driver.find_element('xpath','//div[@class="form-group"][3]/iframe')
driver.switch_to.frame(confirm)
driver.find_element("id",'confirm').send_keys('Admin@1234')
driver.switch_to.parent_frame()

btn=driver.find_element('xpath','//div[@class="form-group"][4]/iframe')
driver.switch_to.frame(btn)
driver.find_element("id",'submitButton').click()
driver.switch_to.parent_frame()

time.sleep(2)

driver.switch_to.default_content()

driver.find_element("xpath",'//a[text()="Window Alert Frame"]').click()
time.sleep(5)

