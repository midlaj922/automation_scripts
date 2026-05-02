class PRACTICE:
    test_login='//a[text()="Test Login Page"]'
    test_table='//a[text()="Test Table"]'

    def __init__(self,driver):
        self.driver=driver

    def test_logi(self):
        self.driver.find_element("xpath",self.test_login).click()

    def test_tabl(self):
        self.driver.find_element("xpath",self.test_table).click()





