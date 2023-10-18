import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class CourseBooking:
    username_field_id = 'email'
    password_field_id = 'pass'
    login_button_selector = 'button[type="submit"]'
    add_course_selector = 'button[class="mat-focus-indicator mat-tooltip-trigger d-block add-course mb-15-md-sm mat-flat-button mat-button-base mat-primary"]'
    find_subject_selector = 'input[placeholder="Find subject"]'
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
        self.driver.find_element(By.CSS_SELECTOR, self.find_subject_selector).send_keys('robotics')
        self.driver.find_element(By.CSS_SELECTOR, self.dropdown_option_selector).click()
    # def selectLanguage(self):
    #     specific_div = self.driver.find_element(By.CSS_SELECTOR, self.language_dropdown_selector)
    #     child_elements = specific_div.find_elements(By.XPATH, ".//*[@id]")
    #     element_ids = [element.get_attribute("id") for element in child_elements]
    #     for i in range(0, len(element_ids)):
    #         # print(element_ids[i])
    #         self.driver.find_element(By.ID, element_ids[i]).click([2])
    #

