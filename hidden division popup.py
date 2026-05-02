import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://www.flipkart.com/')
driver.maximize_window()


driver.find_element("xpath","//input[@title='Search for Products, Brands and More']").send_keys('nike')
time.sleep(2)
driver.find_element("xpath","//ul[@class='GZVzXz GFxnd4 zWhq_n']/li[1]/div/a").click()


time.sleep(3)