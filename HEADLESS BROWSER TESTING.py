import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ob=Options()
ob.add_argument("--headless")
driver = webdriver.Chrome(options=ob)
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui?scenario=1')
driver.maximize_window()

driver.find_element("xpath","//li[text()='Disabled']").click()

dis_ele=driver.find_element("id","name")
time.sleep(2)
driver.execute_script("arguments[0].removeAttribute('disabled')",dis_ele)
dis_ele.send_keys("Lost")
time.sleep(2)