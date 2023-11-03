import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random


# from selenium import webdriver


class CourseBooking:
    username_field_id = 'email'
    password_field_id = 'pass'
    login_button_selector = 'button[type="submit"]'
    add_course_selector = 'button[class="mat-focus-indicator mat-tooltip-trigger d-block add-course mb-15-md-sm mat-flat-button mat-button-base mat-primary"]'
    find_subject_selector = 'input[placeholder="Find subject ..."]'
    dropdown_option_selector = 'div[class="d-flex justify-content-between flex-column-sm"]'
    language_dropdown_selector = 'div[class="mat-form-field-infix ng-tns-c104-12"]'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.username_field_id).clear()
        self.driver.find_element(By.ID, self.username_field_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_selector).click()

    def clickCourseBook(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_course_selector).click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.find_subject_selector).send_keys('robotics')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.dropdown_option_selector).click()

    def selectLanguage(self):
        self.driver.find_element(By.ID, 'mat-select-value-3').click()
        time.sleep(2)
        specific_div = self.driver.find_element(By.ID, 'mat-select-2-panel')
        child_elements = specific_div.find_elements(By.XPATH, ".//*[@id]")
        element_ids = [element.get_attribute("id") for element in child_elements]
        # print(len(element_ids), element_ids)
        random_selection = random.randint(0, 1)
        self.driver.find_element(By.ID, element_ids[random_selection]).click()
    def selectCountry(self):
        self.driver.find_element(By.ID, 'mat-select-value-11').click()
        time.sleep(2)
        specific_div2 = self.driver.find_element(By.ID, 'mat-select-10-panel')
        child_elements2 = specific_div2.find_elements(By.XPATH, ".//*[@id]")
        element_ids2 = [element.get_attribute("id") for element in child_elements2]
        random_selection2 = random.randint(0, len(element_ids2))
        self.driver.find_element(By.ID, element_ids2[random_selection2]).click()
    def selectGrade(self):
        self.driver.find_element(By.ID, 'mat-select-value-13').click()
        time.sleep(2)
        specific_div3 = self.driver.find_element(By.ID, 'mat-select-12-panel')
        child_elements3 = specific_div3.find_elements(By.XPATH, ".//*[@id]")
        element_ids3 = [element.get_attribute("id") for element in child_elements3]
        length3 = len(element_ids3)-1
        random_selection3 = random.randint(0, length3)
        self.driver.find_element(By.ID, element_ids3[random_selection3]).click()
    def addtopic(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Please list a topic you need help with"]').send_keys('topic0001')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/metutors-root/div/div/metutors-request-tutor/div/div/div/div/form/metutors-course-details-form/form/div/div/div[6]/div/h1/button').click()
        self.driver.find_element(By.ID, 'mat-radio-2').click()
    def setDate(self, date):
        self.driver.execute_script('window.scrollBy(0,500);')
        self.driver.find_element(By.ID, 'mat-input-0').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'mat-input-0').send_keys(date)
        self.driver.find_element(By.ID, 'mat-input-0').send_keys(Keys.ESCAPE)
        time.sleep(2)

        self.driver.find_element(By.ID, 'mat-input-1').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'mat-input-1').send_keys(date)
        self.driver.find_element(By.ID, 'mat-input-1').send_keys(Keys.ESCAPE)


