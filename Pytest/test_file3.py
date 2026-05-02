import pytest
@pytest.mark.skip
def test_five():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://www.rolls-roycemotorcars.com/en_GB/home.html")
    driver.maximize_window()
    time.sleep(2)
    driver.close()
@pytest.mark.skip
def test_six():
    import time
    from selenium import webdriver


    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://www.porsche.com/international/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()