import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/datePick/datedropdown?sublist=1')
driver.maximize_window()
driver.find_element('xpath','//input[@placeholder="Select A Date"]').click()
driver.find_element('xpath','//span[@class="react-datepicker__month-read-view--down-arrow"]').click()
month=driver.find_element('xpath','//div[text()="Jul"]')
month.click()
time.sleep(2)
driver.find_element('xpath','//span[@class="react-datepicker__year-read-view--down-arrow"]').click()
year=driver.find_element('xpath','//div[text()="2026"]')
year.click()
time.sleep(2)

dates=driver.find_elements('xpath','//div[@tabindex="-1"]')

for i in dates:
    if i.text == '20':
        i.click()
        break
time.sleep(2)
