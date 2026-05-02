import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

outerframe=driver.find_element('id','singleframe')
driver.switch_to.frame(outerframe)
driver.find_element("xpath",'//input[@type="text"]').send_keys("helllloooo")
time.sleep(5)
driver.switch_to.default_content()
driver.find_element("xpath",'//a[text()="Iframe with in an Iframe"]').click()
frame1=driver.find_element('xpath','//div[@id="Multiple"]/iframe')
driver.switch_to.frame(frame1)
frame2=driver.find_element('xpath','//div[@class="iframe-container"]/iframe')
driver.switch_to.frame(frame2)

driver.find_element("xpath",'//h5[text()="iFrame Demo"][1]/following-sibling::div/div/input').send_keys("helllloooo")
time.sleep(5)
driver.switch_to.default_content()
time.sleep(5)

