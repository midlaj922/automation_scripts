
class Login:
    UN='//input[@placeholder="Username"]'
    PW='//input[@placeholder="Password"]'
    SUB='//button[text()=" Login "]'

    def __init__(self,driver):
        self.driver = driver

    def usr_name(self,data):
        self.driver.find_element("xpath",self.UN).send_keys(data)

    def pwd(self,data):
        self.driver.find_element("xpath",self.PW).send_keys(data)

    def sub_butt(self):
        self.driver.find_element("xpath",self.SUB).click()