import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from UI.locators.profile_page_locators import ProfilePageLocators
import os
from dotenv import load_dotenv

load_dotenv()


class ProfilePage(BasePage):
    def go_to_general_info_section(self):
        general_info = self.browser.find_element(*ProfilePageLocators.SECTION_GENERAL_INFO)
        general_info.click()

    def click_edit_btn(self):
        edit_btn = self.browser.find_element(*ProfilePageLocators.EDIT_BUTTON)
        edit_btn.click()

    def go_to_first_name(self):
        first_name = self.browser.find_element(*ProfilePageLocators.FIRST_NAME)
        first_name.send_keys(Keys.CONTROL + "A")
        first_name.send_keys(Keys.BACK_SPACE)
        first_name.send_keys("Ivanka")

    def go_to_last_name(self):
        last_name = self.browser.find_element(*ProfilePageLocators.LAST_NAME)
        last_name.send_keys(Keys.CONTROL + "A")
        last_name.send_keys(Keys.BACK_SPACE)
        last_name.send_keys("Ivanova")

    def go_to_phone_number(self):
        phone_number = self.browser.find_element(*ProfilePageLocators.PHONE_NUMBER)
        phone_number.send_keys(Keys.CONTROL + "A")
        phone_number.send_keys(Keys.BACK_SPACE)
        phone_number.send_keys("0586907439")

    def click_your_time_zone(self):
        drop_down_your_time_zone = self.browser.find_element(*ProfilePageLocators.YOUR_TIME_ZONE)
        drop_down_your_time_zone.click()

    def choose_your_time_zone(self):
        drop_down_warsaw = self.browser.find_element(*ProfilePageLocators.CHOOSE_YOUR_TIME_ZONE)
        drop_down_warsaw.click()

    def choose_language(self):
        language = self.browser.find_element(*ProfilePageLocators.CHOOSE_LANGUAGE)
        language.click()

    def go_to_add_photo_icon(self):
        add_photo = self.browser.find_element(*ProfilePageLocators.ADD_PHOTO)
        add_photo.click()
        time.sleep(4)
        add_photo.send_keys(r"C:\Users\dombr\PycharmProjects\TeamBook\photo.jpg")

    def confirm_add_photo(self):
        set_as_profile_photo_btn = self.browser.find_element(*ProfilePageLocators.SET_AS_PROFILE_PHOTO_BTN)
        set_as_profile_photo_btn.click()

    def go_to_save_btn(self):
        save_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON_GENERAL_INFO)
        save_btn.click()

    def go_to_email_and_password_section(self):
        section_email_and_password = self.browser.find_element(*ProfilePageLocators.SECTION_EMAIL_AND_PASSWORD)
        section_email_and_password.click()

    def go_to_new_email(self):
        new_email = self.browser.find_element(*ProfilePageLocators.NEW_EMAIL)
        new_email.clear()
        new_email.send_keys(os.environ['NEW_LOGIN'])

    def go_to_save_new_email_btn(self):
        save_new_email_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON_NEW_EMAIL)
        save_new_email_btn.click()

    def go_to_current_password(self):
        current_password = self.browser.find_element(*ProfilePageLocators.CURRENT_PASSWORD)
        current_password.clear()
        current_password.send_keys(os.environ['PASSWORD'])

    def go_to_new_password(self):
        new_password = self.browser.find_element(*ProfilePageLocators.NEW_PASSWORD)
        new_password.clear()
        new_password.send_keys(os.environ['NEW_PASSWORD'])

    def go_to_confirm_new_password(self):
        confirm_new_password = self.browser.find_element(*ProfilePageLocators.CONFIRM_NEW_PASSWORD)
        confirm_new_password.clear()
        confirm_new_password.send_keys(os.environ['NEW_PASSWORD'])

    def go_to_save_new_password_btn(self):
        save_new_password_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON_NEW_PASSWORD)
        save_new_password_btn.click()

    def go_to_schedule_section(self):
        schedule_section = self.browser.find_element(*ProfilePageLocators.SECTION_SCHEDULE)
        schedule_section.click()

    def go_to_saturday_checkbox(self):
        saturday_checkbox = self.browser.find_element(*ProfilePageLocators.SATURDAY_CHECKBOX)
        saturday_checkbox.click()

    def go_to_save_schedule_btn(self):
        save_schedule_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON_SCHEDULE)
        save_schedule_btn.click()

    def go_to_notification_section(self):
        notification = self.browser.find_element(*ProfilePageLocators.SECTION_NOTIFICATIONS)
        notification.click()

    def go_to_operational_planning_checkbox(self):
        operational_planning_checkbox = self.browser.find_element(*ProfilePageLocators.OPERATIONAL_PLANNING_CHECKBOX)
        operational_planning_checkbox.click()

    def go_to_immediate_notifications(self):
        immediate_notifications_radio_button = self.browser.find_element(*ProfilePageLocators.IMMEDIATE_NOTIFICATIONS)
        immediate_notifications_radio_button.click()

    def go_to_capacity_planning_checkbox(self):
        capacity_planning_checkbox = self.browser.find_element(*ProfilePageLocators.CAPACITY_PLANNING_CHECKBOX)
        capacity_planning_checkbox.click()

    def go_to_arrow_up(self):
        arrow_up = self.browser.find_element(*ProfilePageLocators.ARROW_UP)
        arrow_up.click()

    def go_to_actual_time_tracking_checkbox(self):
        actual_time_tracking_checkbox = self.browser.find_element(*ProfilePageLocators.ACTUAL_TIME_TRACKING)
        actual_time_tracking_checkbox.click()

    def go_to_arrow_down(self):
        arrow_down = self.browser.find_element(*ProfilePageLocators.ARROW_DOWN)
        arrow_down.click()

    def do_to_save_notifications_btn(self):
        save_btn = self.browser.find_element(*ProfilePageLocators.SAVE_BUTTON_NOTIFICATIONS)
        save_btn.click()
