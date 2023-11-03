import time
from pageObjects.SignupStudent import SignupStudent
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomData import randomGenerate
from pageObjects.SendFeedback import SendFeedback


class Test_003_feedback:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.logger.info("************* Test_003_Login *********")
        self.logger.info("************* Verifying student feedback ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.feedback = SendFeedback(self.driver)
        self.feedback.setUsername(self.username)
        self.feedback.setPassword(self.password)
        self.feedback.clickLogin()
        time.sleep(5)
        self.feedback.clickFeedback()
        time.sleep(10)
        self.feedback.setStars()
        time.sleep(5)
