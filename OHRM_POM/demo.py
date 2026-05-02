import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"https://www.amazon.in")

driver.find_element("xpath",'//div[@id="nav-tools"]/div[2]/a').click()



