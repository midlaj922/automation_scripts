import pytest

@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.close()
    
