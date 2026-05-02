import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(8)
# driver.get(r'https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=2')
# driver.get(r'https://testautomationpractice.blogspot.com/')
driver.get("https://demoapps.qspiders.com/ui/dragDrop?sublist=0")
driver.maximize_window()
# drag and drop demoapp

# mob_acc=driver.find_element('xpath','//div[text()="Mobile Accessories"]')
# lap_acc=driver.find_element('xpath','//div[text()="Laptop Accessories"]')

# mob_chrger=driver.find_element('xpath','//div[text()="Mobile Charger"]')
# lap_chrger=driver.find_element('xpath','//div[text()="Laptop Charger"]')
# mob_cover=driver.find_element('xpath','//div[text()="Mobile Cover"]')
# lap_cover=driver.find_element('xpath','//div[text()="Laptop Cover"]')
#
ob=ActionChains(driver)
# ob.drag_and_drop(mob_chrger,mob_acc).perform()
# ob.drag_and_drop(lap_chrger,lap_acc).perform()
# ob.drag_and_drop(mob_cover,mob_acc).perform()
# ob.drag_and_drop(lap_cover,lap_acc).perform()
# time.sleep(2)


# drag and drop test test automation

# drag_item=driver.find_element('id','draggable')
# drag_area=driver.find_element('id','droppable')
# ob.drag_and_drop(drag_item,drag_area).perform()
# time.sleep(2)


# drag and drop by offset

ele=driver.find_element('xpath','//div[text()="Drag Me"]')
ob.drag_and_drop_by_offset(ele,200,100).pause(2).perform()
ob.drag_and_drop_by_offset(ele,-200,-100).pause(2).perform()
time.sleep(3)




