import uuid

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

import data
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
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation + 1


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.valid_name_of_team_1, data.valid_name_of_team_2])
def test_add_new_team_positive_boundary_value(browser, login, name):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_team_select()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        team_name_field = browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        team_name_field.send_keys(name)
        page.go_to_create_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
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
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.invalid_name_of_team_1, data.invalid_name_of_team_2,
                                  data.invalid_name_of_team_3, data.invalid_name_of_team_4])
def test_add_new_team_negative(browser, login, name):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_team_select()
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        team_name_field = browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        team_name_field.send_keys(name)
        page.go_to_create_team_btn()
    with allure.step('Verify the error message is displayed'):
        error_message_name = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.ERROR_MESSAGE_NAME)
        )
    text_of_error_message = error_message_name.text
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert text_of_error_message == "Team name must be 3 to 30 characters long."
