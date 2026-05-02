import pytest


@pytest.mark.parametrize('nm',['Mid','Pav'])
def test_one(nm):
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.find_element("id",'name').send_keys(nm)
    time.sleep(2)
    driver.close()


@pytest.mark.parametrize(['nm','em'],[['Mid','Mid@gmail.com'],['Pav','Pav@gmail.com']])
def test_three(nm,em):
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.find_element("id",'name').send_keys(nm)
    driver.find_element("id", 'email').send_keys(em)
    time.sleep(2)
    driver.close()


@pytest.mark.skip
def test_two():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://open.spotify.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.close()
