import uuid

from selenium.webdriver import Keys

import data
import pytest
import allure
from allure_commons.types import AttachmentType

import urls
from UI.pages.profile_page import ProfilePage
from UI.locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Change general info')
@allure.story('Change general info with valid data')
@allure.severity('major')
@pytest.mark.regression
def test_change_general_info_positive(browser, login):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        page.go_to_last_name()
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your profile was successfully updated!"


@allure.feature('Change general info')
@allure.story('Change name in general info, boundary values for first name field')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.valid_first_name_1, data.valid_first_name_2])
def test_change_name_in_general_info_boundary_value_positive(browser, login, name):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        first_name = browser.find_element(*ProfilePageLocators.FIRST_NAME)
        first_name.send_keys(Keys.CONTROL + "A")
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys(name)
        page.go_to_last_name()
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your profile was successfully updated!"


@allure.feature('Change general info')
@allure.story('Change first name in general info, negative boundary value testing')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.invalid_first_name_1, data.invalid_first_name_2])
def test_change_name_in_general_info_boundary_value_negative(browser, login, name):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        first_name = browser.find_element(*ProfilePageLocators.FIRST_NAME)
        first_name.send_keys(Keys.CONTROL + "A")
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys(name)
        page.go_to_last_name()
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change general info')
@allure.story('Change first name in general info, negative values for first name field')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.invalid_first_name_3, data.invalid_first_name_4])
def test_change_name_in_general_info_negative(browser, login, name):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        first_name = browser.find_element(*ProfilePageLocators.FIRST_NAME)
        first_name.send_keys(Keys.CONTROL + "A")
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys(name)
        page.go_to_last_name()
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change general info')
@allure.story('Change last name in general info, boundary values for last name field ')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('surname', [data.valid_last_name_1, data.valid_last_name_2])
def test_change_last_name_in_general_info_boundary_value_positive(browser, login, surname):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        last_name = browser.find_element(*ProfilePageLocators.LAST_NAME)
        last_name.send_keys(Keys.CONTROL + "A")
        last_name.send_keys(Keys.BACK_SPACE)
        last_name.send_keys(surname)
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your profile was successfully updated!"


@allure.feature('Change general info')
@allure.story('Change last name in general info, negative boundary value testing')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('surname', [data.invalid_last_name_1, data.invalid_last_name_2])
def test_change_last_name_in_general_info_boundary_value_negative(browser, login, surname):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        last_name = browser.find_element(*ProfilePageLocators.LAST_NAME)
        last_name.send_keys(Keys.CONTROL + "A")
        last_name.send_keys(Keys.BACK_SPACE)
        last_name.send_keys(surname)
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change general info')
@allure.story('Change last name in general info, negative values for last name field')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('surname', [data.invalid_last_name_3, data.invalid_last_name_4])
def test_change_last_name_in_general_info_negative(browser, login, surname):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        last_name = browser.find_element(*ProfilePageLocators.LAST_NAME)
        last_name.send_keys(Keys.CONTROL + "A")
        last_name.send_keys(Keys.BACK_SPACE)
        last_name.send_keys(surname)
        page.go_to_phone_number()
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change general info')
@allure.story('Change phone in general info, boundary values for phone field')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('phone', [data.valid_phone_1, data.valid_phone_2])
def test_change_phone_in_general_info_boundary_value_positive(browser, login, phone):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        page.go_to_last_name()
        phone_number = browser.find_element(*ProfilePageLocators.PHONE_NUMBER)
        phone_number.send_keys(Keys.CONTROL + "A")
        phone_number.send_keys(Keys.BACK_SPACE)
        phone_number.send_keys(phone)
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e,
                      attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your profile was successfully updated!"


@allure.feature('Change general info')
@allure.story('Change phone in general info, negative boundary value testing')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('phone', [data.invalid_phone_1, data.invalid_phone_2])
def test_change_phone_in_general_info_boundary_value_negative(browser, login, phone):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_general_info_section()
    page.click_edit_btn()
    with allure.step('Change general information'):
        page.go_to_first_name()
        page.go_to_last_name()
        phone_number = browser.find_element(*ProfilePageLocators.PHONE_NUMBER)
        phone_number.send_keys(Keys.CONTROL + "A")
        phone_number.send_keys(Keys.BACK_SPACE)
        phone_number.send_keys(phone)
        page.click_your_time_zone()
        page.choose_your_time_zone()
        page.choose_language()
        # page.go_to_add_photo_icon()
        # page.confirm_add_photo()
        page.go_to_save_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e,
                      attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change email and password')
@allure.story('Change email and password with valid data')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.skip
def test_change_email_and_password_positive(browser, login):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_email_and_password_section()
    with allure.step('Change password'):
        # page.go_to_new_email()
        # page.go_to_save_new_email_btn()
        page.go_to_current_password()
        page.go_to_new_password()
        page.go_to_confirm_new_password()
        page.go_to_save_new_password_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE3)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your password has been successfully updated"


@allure.feature('Change email and password')
@allure.story('Change password with negative values')
@allure.severity('major')
@pytest.mark.regression
@pytest.mark.parametrize('password', [data.invalid_password_profile_1, data.invalid_password_profile_2,
                                      data.invalid_password_profile_3])
def test_change_email_and_password_negative(browser, login, password):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_email_and_password_section()
    with allure.step('Change password'):
        # page.go_to_new_email()
        # page.go_to_save_new_email_btn()
        page.go_to_current_password()
        new_password = browser.find_element(*ProfilePageLocators.NEW_PASSWORD)
        new_password.clear()
        new_password.send_keys(password)
        page.go_to_confirm_new_password()
        page.go_to_save_new_password_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change email and password')
@allure.story('Confirmed password and changed password do not match, negative testing')
@allure.severity('major')
@pytest.mark.regression
def test_change_email_and_password_negative(browser, login):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_email_and_password_section()
    with allure.step('Change password'):
        # page.go_to_new_email()
        # page.go_to_save_new_email_btn()
        page.go_to_current_password()
        new_password = browser.find_element(*ProfilePageLocators.NEW_PASSWORD)
        new_password.clear()
        new_password.send_keys(data.new_password)
        confirm_new_password = browser.find_element(*ProfilePageLocators.CONFIRM_NEW_PASSWORD)
        confirm_new_password.clear()
        confirm_new_password.send_keys(data.confirm_password)
        page.go_to_save_new_password_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_error_message = error_message.text

    assert text_of_error_message == "There was an error:"


@allure.feature('Change schedule')
@allure.story('Change schedule')
@allure.severity('major')
@pytest.mark.regression
def test_change_schedule(browser, login):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_schedule_section()
    page.go_to_saturday_checkbox()
    page.go_to_save_schedule_btn()
    with allure.step("Verify success message is displayed"):
        success_message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE4)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message = success_message.text

    assert text_of_success_message == "Your schedule has been successfully updated"


@allure.feature('Change notifications')
@allure.story('Change notifications')
@allure.severity('major')
@pytest.mark.regression
def test_change_notification(browser, login):
    page = ProfilePage(browser, urls.LINK_PROFILE)
    page.open()
    page.go_to_notification_section()
    page.go_to_operational_planning_checkbox()
    page.go_to_immediate_notifications()
    page.go_to_capacity_planning_checkbox()
    page.go_to_arrow_up()
    page.go_to_actual_time_tracking_checkbox()
    page.go_to_arrow_down()
    page.do_to_save_notifications_btn()
    with allure.step("Verify success message is displayed"):
        success_message2 = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFIlE_SUCCESS_MESSAGE2)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='profile_result' + e, attachment_type=AttachmentType.PNG)
        text_of_success_message2 = success_message2.text

    assert text_of_success_message2 == "Notifications were updated"
