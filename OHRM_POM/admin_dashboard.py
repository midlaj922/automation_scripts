class Admin :

    Add_but='//button[text()=" Add "]'

    def __init__(self,driver):
        self.driver = driver

    def add_clk(self):
        self.driver.find_element('xpath',self.Add_but).click()
