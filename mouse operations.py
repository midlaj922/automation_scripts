import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from fileupload2 import dropdown

driver = webdriver.Chrome()
driver.implicitly_wait(8)
# driver.get(r'https://demoapps.qspiders.com/ui/clickHold?sublist=0')
# driver.get(r'https://demoapps.qspiders.com/ui/mouseHover?sublist=0')
driver.get(r'https://demoapps.qspiders.com/ui/dragDrop?sublist=0')

driver.maximize_window()

# right click
# ele=driver.find_element('id','options')
ob=ActionChains(driver)
# ob.context_click(ele).perform()
#
#
# # double click
# time.sleep(3)
# pp=driver.find_element('xpath','//input[@placeholder="Search..."]')
# pp.send_keys("hai")
# ob.double_click(pp).perform()
#
# time.sleep(3)
#
#
# # click & hold
# cc=driver.find_element("id","circle")
#
# ob.click_and_hold(cc).pause(2).release().perform()
#
# time.sleep(3)


# mouse hover

# ele=driver.find_element('xpath','//img[@class="w-5 h-5 mt-5 ml-3 cursor-pointer "]')
# ob.move_to_element(ele).pause(2).perform()
# time.sleep(4)


# drag and drop
drag=driver.find_element("xpath",'//div[text()="Drag Me"]')
ob.click_and_hold(drag).pause(2).move_by_offset(200,0).pause(2).move_by_offset(-200,0).pause(2).move_by_offset(0,200).pause(2).move_by_offset(0,-200).pause(2).perform()
time.sleep(2)