import time
from Login_page import Login
from Home_page import HomePage
from admin_dashboard import Admin

def testcase(setup):
    driver=setup
    L=Login(driver)
    L.usr_name("Admin")
    L.pwd("admin123")
    L.sub_butt()
    time.sleep(4)
    H=HomePage(driver)
    H.admin_click()
    time.sleep(4)
    D=Admin(driver)
    D.add_clk()
    time.sleep(4)
