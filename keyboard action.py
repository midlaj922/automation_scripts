import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

text=driver.find_element("id","name")
data="skyline"
text.send_keys(data)

ob=ActionChains(driver)

ob.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
ob.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(1)
email=driver.find_element("id","email")
email.click()
time.sleep(1)
ob.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(1)

for i in range(len(data)):
    ob.key_down(Keys.BACKSPACE).perform()
    time.sleep(1)




# scroll by keys

i=0
while i <=5:
    ob.key_down(Keys.PAGE_DOWN).perform()
    time.sleep(1)
    i+=1