import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/browser/newTab?sublist=1')
driver.maximize_window()

driver.find_element('xpath','//h2[text()="Watches"]/following-sibling::button').click()

tab=driver.window_handles
driver.switch_to.window(tab[1])
time.sleep(2)

driver.find_element("xpath",'//button[text()="Add to Cart"]').click()
driver.close()
driver.switch_to.window(tab[0])
# driver.find_element("xpath",'//*[@id="root"]/section/section/svg/g/path').click()
time.sleep(2)