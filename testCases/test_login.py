import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_loginPageTitle(self, setup):
        self.logger.info("*************Test_001_Login*********")
        self.logger.info("*************Verifying Home page title page*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == "Sign in - MEtutors":
            assert True
            self.driver.close()
            self.logger.info("*************Home tile page test is passed*********")
        else:
            self.driver.save_screenshot(
                "/home/mubashar4603/PycharmProjects/Metutors/Screenshots/" + "test_loginPageTitle.png")
            self.driver.close()
            self.logger.error("*************Home title page tes is failed*********")
            assert False

    def test_login(self, setup):
        self.logger.info("*************Verifying login test*********")
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
            self.logger.info("*************Login test is passed*********")
        else:
            self.driver.save_screenshot("/home/mubashar4603/PycharmProjects/Metutors/Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("*************Login test is failed*********")
            assert False


