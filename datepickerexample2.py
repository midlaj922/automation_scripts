import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/datePick?sublist=0')
driver.maximize_window()
driver.find_element('xpath','//input[@placeholder="Select A Date"]').click()
while True:


    monthyear=driver.find_element('xpath','//div[@class="react-datepicker__current-month"]').text
    if monthyear=='July 2025':
        break
    else:
        driver.find_element('xpath','//button[@aria-label="Previous Month"]').click()



dates=driver.find_elements('xpath','//div[@tabindex="-1"]')

for i in dates:
    if i.text == '20':
        i.click()
        break
time.sleep(2)
