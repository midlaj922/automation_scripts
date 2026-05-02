class LOGIN:
      UN='username'
      PWD='password'
      sub='submit'
      def __init__(self,driver):
          self.driver=driver


      def UN_TXT(self,data):
          self.driver.find_element("id",self.UN).send_keys(data)

      def PWD_TXT(self,data):
          self.driver.find_element("id",self.PWD).send_keys(data)

      def SUB_click(self):
          self.driver.find_element("id",self.sub).click()

