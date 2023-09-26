import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class SignupStudent:
    signup_button_selector = 'a[href="/signup"]'
    textbox_fname_id = 'firstName'
    textbox_lname_id = 'lastName'
    textbox_email_id = 'email'
    textbox_phone_id = 'phone'
    textbox_password_id = 'pass'
    textbox_Cpassword_id = 'pass2'
    checkbox_selector = 'span[class="mat-checkbox-inner-container"]'
    create_button_seletor = 'button[type="submit"]'
    def __init__(self, driver):
        self.driver = driver
    def clickSignup(self):
        self.driver.find_element(By.CSS_SELECTOR, self.signup_button_selector).click()
    def setFname(self, fname):
        self.driver.find_element(By.ID, self.textbox_fname_id).send_keys(fname)
    def setLname(self,lname):
        self.driver.find_element(By.ID, self.textbox_lname_id).send_keys(lname)
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
    def setPhone(self, phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.ID, self.textbox_Cpassword_id).send_keys(password)
    def checkBox(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_selector).click()
    def clickCreate(self):
        self.driver.find_element(By.CSS_SELECTOR, self.create_button_seletor)
