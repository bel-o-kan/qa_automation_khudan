from selenium.webdriver import Chrome
from less_23.pages.dashboard_page import Dashboard

import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('lesson23/drivers/chromedriver.exe')
    driver.get("https://epicentrk.ua/")
    # print(driver.get_cookies())
    # for cookie in driver.get_cookies():
    #     print(cookie)
    # token_xsrf = "XSRF-TOKEN"
    # driver.add_cookie({'name':'test', 'value':'test'})
    # driver.get_cookie("test")
    # driver.delete_cookie('test')
    # driver.delete_all_cookies()
    # print(driver.get_cookies())
    driver.execute_script("window.localStorage['test'] = 'Test_value'")
    print(type(driver.execute_script("return window.localStorage['esState'];")))

    yield driver

    driver.quit()

@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)