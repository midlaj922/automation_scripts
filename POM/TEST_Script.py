from LOGIN_PAGE import LOGIN
from HOME_PAGE import HOME
from Practice import PRACTICE

def test_case(setup):
    driver=setup
    L=LOGIN(driver)
    L.UN_TXT("student")
    L.PWD_TXT("Password123")
    L.SUB_click()
    H=HOME(driver)
    H.practice_click()
    P=PRACTICE(driver)
    P.test_tabl()``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````