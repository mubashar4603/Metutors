from selenium import webdriver
import pytest
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("------------Launching the chrome browser..........")
    elif browser=='firefox':
        print("------------Launching the firefox browser...........")
        driver = webdriver.Firefox()
    elif browser=='edge':
        driver = webdriver.Edge()
        print("Launching the firefox browser...........")
    else:
        driver=webdriver.Chrome()
    return  driver
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")