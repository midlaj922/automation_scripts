import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://www.irctc.co.in/nget/train-search')
driver.maximize_window()

driver.find_element('xpath','//button[text()="OK"]').click()
driver.find_element('xpath','//a[text()=" HOTELS "]').click()
time.sleep(3)
tab=driver.window_handles
driver.switch_to.window(tab[1])
time.sleep(5)
driver.find_element('xpath','//input[@id="inputbox"]').send_keys('wayan')
time.sleep(3)
driver.find_element('xpath','//div[@id="autofillId"]/ul/li/a').click()

# driver.find_element('xpath','//input[@placeholder="Check-in Date"]').click()
#
#
# driver.find_element('xpath','//button[@class="current ng-star-inserted"]').click()
#
# # finding the month

# row=driver.find_elements('xpath','//table[@role="grid"]/tbody/tr')
# col=driver.find_elements('xpath','//table[@role="grid"]/tbody/tr/td')
# time.sleep(3)
# # for i in range(len(row)):
#     for j in range(len(col)):
#         data=driver.find_element('xpath',f'//table[@role="grid"]/tbody/tr[{i}/td[{j}]')
#         if data.text=="July":
#             data.click()
#             break
time.sleep(3)



driver.find_element('xpath','//div[@class="SearchBoxMain"]/form/div/div[5]/button').click()
time.sleep(3)
driver.switch_to.window(tab[0])
time.sleep(3)