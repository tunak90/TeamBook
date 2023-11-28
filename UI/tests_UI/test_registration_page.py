import pytest

import urls
from UI.pages.registration_page import RegistrationPage
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser
import allure


@allure.feature('Registration')
@allure.story('Registration with valid email and valid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.skip
def test_registration_positive(browser):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with valid email'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        page.go_to_reg_business_email()
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
        page.go_to_reg_skip_btn()
    with allure.step("Verify user_menu is displayed"):
        user_menu = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
        )

    assert user_menu.is_displayed()


@allure.feature('Registration')
@allure.story('Registration with invalid email and valid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('email', ['test@gmail.com', 'testgmail.com'])
def test_registration_negative_email(browser, email):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with invalid email: {email}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        page.go_to_reg_business_email()
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
        )

    assert error_message.is_displayed()


@allure.feature('Registration')
@allure.story('Registration with valid email and invalid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('password', ['A123456', '12345678', 'sdfghjklcvb'])
def test_registration_negative_password(browser, password):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with invalid password: {password}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        page.go_to_reg_business_email()
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
        )

    assert error_message.is_displayed()
