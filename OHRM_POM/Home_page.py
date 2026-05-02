class HomePage:
    Adm='//div[@id="app"]/div/div/aside/nav/div/ul/li/a'

    def __init__(self,driver):
        self.driver=driver
    def admin_click(self):
        self.driver.find_element('xpath',self.Adm).click()

