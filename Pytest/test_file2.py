import pytest
@pytest.mark.skip
def test_three():
    import time
    from selenium import webdriver


    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://www.nike.in/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()

@pytest.mark.skip
def test_four():
    import time
    from selenium import webdriver
    from selenium.webdriver import ActionChains

    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://www.samsung.com/in/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()