import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1')
driver.maximize_window()
prod=driver.find_element('xpath','//select[@id="select-multiple-native"]')
obj1=Select(prod)
obj1.select_by_visible_text('Fjallraven - Foldsac...')
obj1.select_by_visible_text('Mens Casual Premium ...')
obj1.select_by_visible_text('Mens Casual Slim Fit...')

driver.find_element('xpath','//button[contains(text(),"Add")]').click()
time.sleep(2)