from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage:
    textbox_username_id = "email"
    textbox_password_id = "pass"
    button_login_selector = 'button[type="submit"]'
    popup_logout_selector = 'div[class="mat-menu-trigger user-nav"]'
    option_logout_xpath = '//*[@id="mat-menu-panel-7"]/div/button[3]'
    def __init__(self, driver):
        self.driver = driver
    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_selector).click()