class HOME:
    practice='//a[text()="Practice"]'
    contact='//a[text()="Contact"]'
    def __init__(self,driver):
        self.driver = driver

    def practice_click(self):
        self.driver.find_element('xpath',self.practice).click()

    def logout_click(self):
        self.driver.find_element('xpath',self.contact).click()
