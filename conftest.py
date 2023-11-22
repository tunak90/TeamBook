import pytest
from selenium import webdriver
from UI.pages.login_page import LoginPage
from UI.locators.login_page_locators import LoginPageLocators
from UI.locators.planning_page_locators import PlanningPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    link = "https://web.teambooktest.com/login"
    page = LoginPage(browser, link)
    page.open()
    driver = webdriver.Chrome()
    driver.get(link)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(*LoginPageLocators.LOGIN_EMAIL)
    )
    page.go_to_login_email()
    page.go_to_login_password()
    page.go_to_login_btn()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(*PlanningPageLocators.USER_MENU)
    )
