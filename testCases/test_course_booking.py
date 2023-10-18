import time
from pageObjects.SignupStudent import SignupStudent
from utilities.readProperties import ReadConfig
class Test_002_Login:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    def test_courseBooking(self):
        self.logger.info("************* Test_000_Login *********")
        self.logger.info("************* Verifying student course booking ********")
