import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    def test_loginPageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == "Sign in - MEtutors":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/mubashar4603/PycharmProjects/Metutors/Screenshots/"+"test_loginPageTitle.png")
            self.driver.close()
            assert False
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(6)
        actual_title = self.driver.title
        if actual_title == "Dashboard - MEtutors":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/mubashar4603/PycharmProjects/Metutors/Screenshots/"+"test_login.png")
            self.driver.close()
            assert False

