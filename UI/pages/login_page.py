from .base_page import BasePage
from UI.locators.login_page_locators import LoginPageLocators
import os
from dotenv import load_dotenv

load_dotenv()


class LoginPage(BasePage):
    def go_to_login_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.clear()
        login_email.send_keys(os.environ['LOGIN'])

    def go_to_login_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.clear()
        login_password.send_keys(os.environ['PASSWORD'])

    def go_to_login_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()

    def go_to_registration(self):
        link_to_registration = self.browser.find_element(*LoginPageLocators.LINK_TO_REGISTRATION_PAGE)
        link_to_registration.click()
