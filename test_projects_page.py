import time
import uuid

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys

import data
import urls
from UI.pages.projects_page import ProjectsPage
from UI.locators.projects_page_locators import ProjectsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Create a project')
@allure.story('Create a project with valid data')
@allure.severity('critical')
@pytest.mark.regression
def test_create_project_positive(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_create_project()
    with allure.step("Enter data"):
        page.go_to_name()
        page.go_to_short_name()
        page.go_to_client_drop_down_list()
        page.choose_client()
        page.go_to_analytics_drop_down_list()
        page.choose_billable()
        page.go_to_estimated_hours()
        page.go_to_manager_drop_down_list()
        page.choose_person()
        page.go_to_status_drop_down_list()
        page.choose_to_be_confirmed()
        page.go_to_start_date_checkbox()
        page.click_calendar()
        date_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ProjectsPageLocators.CHOOSE_DATE)
        )
        date_element.click()
        page.go_to_end_date_checkbox()
        page.go_to_create_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProjectsPageLocators.PROJECT_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Project Dental Clinic [Dent Cl] was created successfully"


@allure.feature('Create a project')
@allure.story('Create a project with valid data but already exists')
@allure.severity('critical')
@pytest.mark.regression
def test_create_project_but_exists(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_create_project()
    with allure.step("Enter data"):
        page.go_to_name()
        page.go_to_short_name()
        page.go_to_client_drop_down_list()
        page.choose_client()
        page.go_to_analytics_drop_down_list()
        page.choose_billable()
        page.go_to_estimated_hours()
        page.go_to_manager_drop_down_list()
        page.choose_person()
        page.go_to_status_drop_down_list()
        page.choose_to_be_confirmed()
        page.go_to_start_date_checkbox()
        page.click_calendar()
        date_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ProjectsPageLocators.CHOOSE_DATE)
        )
        date_element.click()
        page.go_to_end_date_checkbox()
        page.go_to_create_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProjectsPageLocators.PROJECT_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "There was an error:"


@allure.feature('Create a project')
@allure.story('Create a project with invalid project name')
@allure.severity('minor')
@pytest.mark.parametrize('name', [data.invalid_project_name_1, data.invalid_project_name_2, data.invalid_project_name_3,
                                  data.invalid_project_name_4])
def test_create_project_negative_name_field(browser, login, name):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_create_project()
    with allure.step("Enter data"):
        name_element = browser.find_element(*ProjectsPageLocators.NAME)
        name_element.clear()
        name_element.send_keys(name)
        page.go_to_short_name()
        page.go_to_client_drop_down_list()
        page.choose_client()
        page.go_to_analytics_drop_down_list()
        page.choose_billable()
        page.go_to_estimated_hours()
        page.go_to_manager_drop_down_list()
        page.choose_person()
        page.go_to_status_drop_down_list()
        page.choose_to_be_confirmed()
        page.go_to_start_date_checkbox()
        page.click_calendar()
        date_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ProjectsPageLocators.CHOOSE_DATE)
        )
        date_element.click()
        page.go_to_end_date_checkbox()
        page.go_to_create_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProjectsPageLocators.PROJECT_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "There was an error:"


@allure.feature('Create a project')
@allure.story('Create a project with invalid project short name')
@allure.severity('minor')
@pytest.mark.parametrize('shortname', [data.invalid_project_short_name_1, data.invalid_project_short_name_2,
                                       data.invalid_project_short_name_3])
def test_create_project_negative_short_name_field(browser, login, shortname):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_create_project()
    with allure.step("Enter data"):
        page.go_to_name()
        short_name = browser.find_element(*ProjectsPageLocators.SHORT_NAME)
        short_name.clear()
        short_name.send_keys(shortname)
        page.go_to_client_drop_down_list()
        page.choose_client()
        page.go_to_analytics_drop_down_list()
        page.choose_billable()
        page.go_to_estimated_hours()
        page.go_to_manager_drop_down_list()
        page.choose_person()
        page.go_to_status_drop_down_list()
        page.choose_to_be_confirmed()
        page.go_to_start_date_checkbox()
        page.click_calendar()
        date_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ProjectsPageLocators.CHOOSE_DATE)
        )
        date_element.click()
        page.go_to_end_date_checkbox()
        page.go_to_create_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProjectsPageLocators.PROJECT_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "There was an error:"


@allure.feature('Edit a project')
@allure.story('Edit a project')
@allure.severity('major')
@pytest.mark.regression
def test_edit_project(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_project_dental_clinic()
    page.go_to_edit_project_btn()
    estimated_hours = browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS)
    estimated_hours.send_keys(Keys.CONTROL + "A")
    estimated_hours.send_keys(Keys.BACK_SPACE)
    estimated_hours.send_keys("220")
    page.go_to_save_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ProjectsPageLocators.PROJECT_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Project was updated successfully"


@allure.feature('Delete a project')
@allure.story('Delete a project')
@allure.severity('major')
@pytest.mark.regression
def test_delete_project(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_project_dental_clinic()
    page.go_to_archive_btn()
    page.go_to_confirm_archive_btn()
    page.go_to_archived_drop_down_list()
    page_with_archived_projects = WebDriverWait(browser, 10).until(

        EC.presence_of_element_located(ProjectsPageLocators.CHOOSE_ARCHIVED)
    )
    page_with_archived_projects.click()
    projects_before = len(browser.find_elements(*ProjectsPageLocators.PROJECT_LIST))
    page.go_to_project_dental_clinic()
    page.click_delete()
    page.click_confirm_delete_btn()
    time.sleep(5)
    projects_after = len(browser.find_elements(*ProjectsPageLocators.PROJECT_LIST))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='project_result' + e, attachment_type=AttachmentType.PNG)
    assert projects_before != projects_after


@allure.feature('Create a client')
@allure.story('Create a client')
@allure.severity('critical')
@pytest.mark.regression
def test_create_client_positive(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_manage_clients()
    page.go_to_new_client()
    page.go_to_client_name()
    page.go_to_client_email()
    page.go_to_client_phone()
    page.go_to_save_new_client_btn()


@allure.feature('Edit a client')
@allure.story('Edit a client')
@allure.severity('critical')
@pytest.mark.regression
def test_edit_client(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_manage_clients()
    page.go_to_new_client()
    page.go_to_client_name()
    client_email = browser.find_element(*ProjectsPageLocators.EMAIL_CLIENT)
    client_email.send_keys(Keys.CONTROL + "A")
    client_email.send_keys(Keys.BACK_SPACE)
    client_email.send_keys("noris123@mail.ru")
    page.go_to_client_phone()
    page.go_to_save_new_client_btn()


@allure.feature('Delete a client')
@allure.story('Delete a client')
@allure.severity('critical')
@pytest.mark.regression
def test_delete_client(browser, login):
    page = ProjectsPage(browser, urls.LINK_PROJECTS)
    page.open()
    page.go_to_manage_clients()
    page.go_to_client()
    page.go_to_delete_btn()
    page.confirm_delete_btn()
