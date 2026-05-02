
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
time.sleep(3)
driver.maximize_window()
driver.find_element("xpath","/html/body/div[1]/div/div[2]/section/main/section/article[1]/aside/article/aside[2]/div/div/form/div[1]/input").send_keys("PavanKarthik")
time.sleep(3)
driver.find_element("xpath","/html/body/div[1]/div/div[2]/section/main/section/article[1]/aside/article/aside[2]/div/div/form/div[2]/input").send_keys("PavanKarthik@gmail.com")
time.sleep(3)
driver.find_element("xpath","/html/body/div[1]/div/div[2]/section/main/section/article[1]/aside/article/aside[2]/div/div/form/div[3]/section/input").send_keys("Pavan@123")
time.sleep(3)
driver.find_element("xpath","/html/body/div[1]/div/div[2]/section/main/section/article[1]/aside/article/aside[2]/div/div/form/div[4]/button").click()
time.sleep(3)

