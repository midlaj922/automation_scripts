import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/dropdown?sublist=0')
driver.maximize_window()
country=driver.find_element('xpath','//select[@id="select3"]')
obj1=Select(country)
country_opt=obj1.options
obj1.select_by_visible_text('India')
# state
state=driver.find_element('xpath','//select[@id="select5"]')
obj2=Select(state)
obj2.select_by_value('Kerala')

city=driver.find_element('xpath','//label[@for="cities"]/following-sibling::select')
obj3=Select(city)
obj3.select_by_value('Wayanad')
time.sleep(3)