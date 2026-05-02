import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()
dropdowns=driver.find_element('xpath','//select[@id="colors"]')
obj=Select(dropdowns)

#to get all the option with text
opt=obj.options
for option in opt:
    print(option.text)


# to select a particular option with select()

obj.select_by_index(1)
obj.select_by_value('green')
obj.select_by_visible_text('Yellow')
first=obj.first_selected_option
print()
print(first.text)
selected=obj.all_selected_options
for i in selected:
    print(i.text)
obj.deselect_all()

time.sleep(3)