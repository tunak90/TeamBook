import pytest

import urls
from UI.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI.locators.login_page_locators import LoginPageLocators
from UI.locators.registration_page_locators import RegistrationPageLocators
from UI.locators.planning_page_locators import PlanningPageLocators

import os


def test_login_positive(browser):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    # WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL)
    # )
    page.go_to_login_email()
    page.go_to_login_password()
    page.go_to_login_btn()
    user_menu = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
    )

    assert user_menu.is_displayed()


# def test_login_negative(browser):
#     page = LoginPage(browser, os.environ['LINK_LOGIN'])
#     page.open()
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL)
#     )
#     page.go_to_login_email()
#     page.go_to_login_password()
#     page.go_to_login_btn()
#     error_message = WebDriverWait(browser, 10).until(
#            EC.presence_of_element_located(LoginPageLocators.LOGIN_ERROR_MESSAGE)
#     )
#
#     assert error_message.is_displayed()


def test_go_to_registration_page(browser):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(LoginPageLocators.LINK_TO_REGISTRATION_PAGE)
    )
    page.go_to_registration()
    reg_first_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegistrationPageLocators.REG_FIRST_NAME)
    )

    assert reg_first_name.is_displayed()
