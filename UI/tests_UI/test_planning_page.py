import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

import urls
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.pages.planning_page import PlanningPage


# @pytest.mark.regression
# def test_add_user(browser, login):
#     page = PlanningPage(browser, urls.LINK_PLANNING)
#     page.open()
#     page.go_to_add_user()
#     page.go_to_select_user_field()
#     create_new_user = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located(PlanningPageLocators.CREATE_NEW_USER)
#     )
#     create_new_user.click()


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
def test_add_new_team_positive(browser, login):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_team_select()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        page.go_to_team_name_field()
        page.go_to_create_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name="result10", attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation + 1


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
def test_add_new_team_but_cancel(browser, login):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_team_select()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        page.go_to_team_name_field()
        page.go_to_cancel_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name="result111", attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation
