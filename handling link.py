import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://www.nike.com/in/')
driver.maximize_window()
link=driver.find_elements('tag name',"a")

for i in link:
    print(i.text)

print(len(link))

for i in link:
    if i.text=='Men':
        i.click()
        break


