import time
import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# print the no of dropdown
# dropdowns=driver.find_elements('tag name','select')
# print(len(dropdowns))

# to count and print the no of option inside the dropdowns
options=driver.find_elements('xpath','//select[@id="colors"]/option')
print(len(options))

for i in options:
    print(i.text)


# to select a option from dropdown
for i in options:
    if i.text == 'Blue':
        i.click()
        break

time.sleep(3)

driver.find_element('xpath','//select[@id="colors"]').click()
time.sleep(2)
driver.find_element('xpath','//select/option[@value="yellow"]').click()
driver.find_element('xpath','//select[@id="colors"]').click()
time.sleep(5)