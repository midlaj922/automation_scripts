import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

checkbox=driver.find_elements('xpath',"//input[@type='checkbox']")
print("check box",len(checkbox))

days=driver.find_elements('xpath',"//input[@type='checkbox' and @class]")
print("radio button",len(days))

for i in days:
    i.click()
    time.sleep(1)


for i in days[::-1]:
    i.click()
    time.sleep(1)

for i in days[:3:]:
    i.click()
    time.sleep(1)

for i in days:
    if i.get_attribute('id') in ['sunday','monday']:
         i.click()

radio_button =driver.find_elements('xpath',"//input[type='radio']")

for i in radio_button:
    if i.get_attribute('id') =='male':
        i.click()
        break
