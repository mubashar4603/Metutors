import time
from pageObjects.SignupStudent import SignupStudent
from utilities.readProperties import ReadConfig
from utilities.randomData import randomGenerate
from utilities.getOTP import getOTP
from utilities.customLogger import LogGen

class Test_000_Login:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getEmail()
    fname = ReadConfig.getFname()
    lname = ReadConfig.getLname()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    def test_signup_student(self, setup):
        self.logger.info("************* Test_000_Login *********")
        self.logger.info("************* Verifying student signup ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.signup_student = SignupStudent(self.driver)
        self.signup_student.clickSignup()
        time.sleep(2)
        self.signup_student.setFname(self.fname)
        self.signup_student.setLname(self.lname)
        self.signup_student.setEmail(randomGenerate.add_random_numbers_to_email(self.email))
        self.signup_student.setPhone(randomGenerate.generate_random_phone_number())
        self.signup_student.setPassword(self.password)
        self.driver.execute_script('window.scrollBy(0,500);')
        time.sleep(2)
        self.signup_student.checkBox()
        time.sleep(2)
        self.signup_student.clickCreate()
        time.sleep(15)
        # req_otp = getOTP.access_email(username = 'mubashar4603@gmail.com', password = 'lfst wacj qiwp wclj')
        req_otp = 4
        self.signup_student.putOTP(req_otp)
        time.sleep(10)




        time.sleep(10)



