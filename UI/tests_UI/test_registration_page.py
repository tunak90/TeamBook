import urls
from UI.pages.registration_page import RegistrationPage
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.locators.registration_page_locators import RegistrationPageLocators
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser


# def test_registration_positive(browser):
#     page = RegistrationPage(browser, urls.LINK_REGISTRATION)
#     page.open()
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located(RegistrationPageLocators.REG_FIRST_NAME)
#     )
#     page.go_to_reg_first_name()
#     page.go_to_reg_last_name()
#     page.go_to_reg_business_email()
#     page.go_to_reg_organization()
#     page.go_to_reg_password()
#     page.go_to_reg_checkbox()
#     page.go_to_reg_create_org_btn()
#     page.go_to_reg_skip_btn()
#     user_menu = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
#     )
#
#     assert user_menu.is_displayed()


def test_registration_negative(browser):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegistrationPageLocators.REG_FIRST_NAME)
    )
    page.go_to_reg_first_name()
    page.go_to_reg_last_name()
    page.go_to_reg_business_email()
    page.go_to_reg_organization()
    page.go_to_reg_password()
    page.go_to_reg_checkbox()
    page.go_to_reg_create_org_btn()
    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
    )

    assert error_message.is_displayed()
