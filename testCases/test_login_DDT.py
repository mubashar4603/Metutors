import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import utilXL

class Test_002_Login_DDT:
    baseURL = ReadConfig.getAppURL()
    path = "/home/mubashar4603/PycharmProjects/Metutors/TestData/metutor.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************* Test_001_Login_DDT *********")
        self.logger.info("************* Verifying login test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.rows = utilXL.getRows(self.path, 'Sheet1')
        print("Total number of rows in excel:",self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = utilXL.readData(self.path, 'Sheet1', r, 1)
            self.password = utilXL.readData(self.path, 'Sheet1', r, 2)
            self.exp = utilXL.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(6)
            actual_title = self.driver.title
            exp_title = "Dashboard - MEtutors"
            if actual_title == exp_title:
                print(self.exp)
                if self.exp == "pass":
                    self.logger.info("****** passed ****")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("****** failed *****")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif actual_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***** failed *****")
                    lst_status.append("fail")
                elif self.exp == 'fail':
                    self.logger.info("***** passed *****")
                    lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("**** Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Lgin DDT test failed ******")
            self.driver.close()
            assert False


