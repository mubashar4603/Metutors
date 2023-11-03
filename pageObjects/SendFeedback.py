import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random


# from selenium import webdriver


class SendFeedback:
    username_field_id = 'email'
    password_field_id = 'pass'
    login_button_selector = 'button[type="submit"]'
    feedback_button_selector = 'button[class="mat-focus-indicator float-end ms-2 mb-15-sm mat-flat-button mat-button-base mat-primary"]'
    stars_id0 = 'star3-0'
    stars_id1 = 'star3-1'
    stars_id2 = 'star3-2'
    stars_id3 = 'star3-3'
    stars_id4 = 'star3-4'

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

    def clickFeedback(self):
        self.driver.find_element(By.CSS_SELECTOR, self.feedback_button_selector).click()

    def setStars(self):
        self.driver.find_element(By.ID, self.stars_id0).click()
        # self.driver.find_element(By.ID, self.stars_id1).click()
        # self.driver.find_element(By.ID, self.stars_id2).click()
        # self.driver.find_element(By.ID, self.stars_id3).click()
        # self.driver.find_element(By.ID, self.stars_id4).click()
