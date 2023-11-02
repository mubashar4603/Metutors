import time
from pageObjects.SignupStudent import SignupStudent
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomData import randomGenerate
from pageObjects.CourseBooking import CourseBooking


class Test_002_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    def test_courseBooking(self, setup):
        self.logger.info("************* Test_000_Login *********")
        self.logger.info("************* Verifying student course booking ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.course_book = CourseBooking(self.driver)
        self.course_book.setUsername(self.username)
        self.course_book.setPassword(self.password)
        self.course_book.clickLogin()
        time.sleep(5)
        self.course_book.clickCourseBook()
        time.sleep(3)
        self.course_book.selectLanguage()
        time.sleep(3)
        self.course_book.selectCountry()
        time.sleep(3)
        self.course_book.selectGrade()
        time.sleep(3)
        self.course_book.addtopic()
        self.driver.execute_script('window.scrollBy(0,500);')
        time.sleep(3)
        self.course_book.setDate(randomGenerate.generate_random_date())
        time.sleep(5)


