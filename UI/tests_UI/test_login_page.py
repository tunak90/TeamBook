import allure
import pytest

import urls
from UI.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI.locators.login_page_locators import LoginPageLocators
from UI.locators.registration_page_locators import RegistrationPageLocators
from UI.locators.planning_page_locators import PlanningPageLocators


@allure.feature('login')
@allure.story('Login with valid email and valid password')
@allure.severity('blocker')
@pytest.mark.smoke
@pytest.mark.regression
def test_login_positive(browser):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    with allure.step('Login with valid email'):
        page.go_to_login_email()
        page.go_to_login_password()
        page.go_to_login_btn()
    with allure.step("Verify user_menu is displayed"):
        user_menu = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
        )

    assert user_menu.is_displayed()


@allure.feature('login')
@allure.story('Login with invalid email and valid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('email', ['12345@gmail.com', '@gmail.com', 'testgmail.com'])
def test_login_negative_email(browser, email):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    with allure.step(f'Login with invalid email: {email}'):
        page.go_to_login_email()
        page.go_to_login_password()
        page.go_to_login_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located(LoginPageLocators.LOGIN_ERROR_MESSAGE)
        )

    assert error_message.is_displayed()


@allure.feature('login')
@allure.story('Login with valid email and invalid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('password', ['a1234567!', 'A1234567'])
def test_login_negative_password(browser, password):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    with allure.step(f'Login with invalid password: {password}'):
        page.go_to_login_email()
        page.go_to_login_password()
        page.go_to_login_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_ERROR_MESSAGE)
        )

    assert error_message.is_displayed()


@allure.feature('registration')
@allure.severity('blocker')
@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_registration_page(browser):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    with allure.step('Go to the registration page'):
        page.go_to_registration()
    with allure.step("Verify reg_first_name is displayed"):
        reg_first_name = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_FIRST_NAME)
        )

    assert reg_first_name.is_displayed()
