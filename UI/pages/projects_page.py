from .base_page import BasePage
from UI.locators.projects_page_locators import ProjectsPageLocators


class ProjectsPage(BasePage):
    def go_to_create_project(self):
        create_project = self.browser.find_element(*ProjectsPageLocators.CREATE_PROJECT)
        create_project.click()

    def go_to_name(self):
        name = self.browser.find_element(*ProjectsPageLocators.NAME)
        name.clear()
        name.send_keys("Dental Clinic")

    def go_to_short_name(self):
        short_name = self.browser.find_element(*ProjectsPageLocators.SHORT_NAME)
        short_name.clear()
        short_name.send_keys("Dent Cl")

    def go_to_client_drop_down_list(self):
        client = self.browser.find_element(*ProjectsPageLocators.CLIENT_DROP_DOWN_LIST)
        client.click()

    def choose_client(self):
        salvor_client = self.browser.find_element(*ProjectsPageLocators.SALVOR_CLIENT)
        salvor_client.click()

    def go_to_analytics_drop_down_list(self):
        analytics = self.browser.find_element(*ProjectsPageLocators.ANALYTICS_DROP_DOWN_LIST)
        analytics.click()

    def choose_billable(self):
        billable = self.browser.find_element(*ProjectsPageLocators.BILLABLE)
        billable.click()

    def go_to_estimated_hours(self):
        estimated_hours = self.browser.find_element(*ProjectsPageLocators.ESTIMATED_HOURS)
        estimated_hours.send_keys("200")

    def go_to_manager_drop_down_list(self):
        manager = self.browser.find_element(*ProjectsPageLocators.MANAGER_DROP_DOWN_LIST)
        manager.click()

    def choose_person(self):
        person = self.browser.find_element(*ProjectsPageLocators.PERSON)
        person.click()

    def go_to_status_drop_down_list(self):
        status = self.browser.find_element(*ProjectsPageLocators.STATUS_DROP_DOWN_LIST)
        status.click()

    def choose_to_be_confirmed(self):
        to_be_confirmed = self.browser.find_element(*ProjectsPageLocators.TO_BE_CONFIRMED)
        to_be_confirmed.click()

    def go_to_start_date_checkbox(self):
        start_date = self.browser.find_element(*ProjectsPageLocators.START_DATE_CHECKBOX)
        start_date.click()

    def click_calendar(self):
        click_calendar = self.browser.find_element(*ProjectsPageLocators.CLICK_ON_CALENDAR)
        click_calendar.click()

    def go_to_end_date_checkbox(self):
        end_date = self.browser.find_element(*ProjectsPageLocators.END_DATE_CHECKBOX)
        end_date.click()

    def go_to_create_btn(self):
        create_btn = self.browser.find_element(*ProjectsPageLocators.CREATE_BTN)
        create_btn.click()

    def go_to_project_dental_clinic(self):
        project = self.browser.find_element(*ProjectsPageLocators.PROJECT)
        project.click()

    def go_to_edit_project_btn(self):
        edit_project_btn = self.browser.find_element(*ProjectsPageLocators.EDIT_PROJECT_BTN)
        edit_project_btn.click()

    def go_to_save_btn(self):
        save_btn = self.browser.find_element(*ProjectsPageLocators.SAVE_BTN)
        save_btn.click()

    def go_to_archive_btn(self):
        archive_btn = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_BTN)
        archive_btn.click()

    def go_to_confirm_archive_btn(self):
        confirm_archive_btn = self.browser.find_element(*ProjectsPageLocators.CONFIRM_ARCHIVE_BTN)
        confirm_archive_btn.click()

    def go_to_archived_drop_down_list(self):
        archived_drop_down_list = self.browser.find_element(*ProjectsPageLocators.ARCHIVE_DROP_DOWN_LIST)
        archived_drop_down_list.click()

    def choose_archived(self):
        archived = self.browser.find_element(*ProjectsPageLocators.CHOOSE_ARCHIVED)
        archived.click()

    def go_to_check_box(self):
        check_box = self.browser.find_element(*ProjectsPageLocators.CHECK_BOX)
        check_box.click()

    def click_delete(self):
        delete_btn = self.browser.find_element(*ProjectsPageLocators.DELETE_BTN)
        delete_btn.click()

    def click_confirm_delete_btn(self):
        confirm_delete_btn = self.browser.find_element(*ProjectsPageLocators.CONFIRM_DELETE_BTN)
        confirm_delete_btn.click()

    def go_to_manage_clients(self):
        manage_clients = self.browser.find_element(*ProjectsPageLocators.MANAGE_CLIENTS)
        manage_clients.click()

    def go_to_new_client(self):
        new_client = self.browser.find_element(*ProjectsPageLocators.NEW_CLIENT)
        new_client.click()

    def go_to_client_name(self):
        client_name = self.browser.find_element(*ProjectsPageLocators.NAME_CLIENT)
        client_name.clear()
        client_name.send_keys("Noris")

    def go_to_client_email(self):
        client_email = self.browser.find_element(*ProjectsPageLocators.EMAIL_CLIENT)
        client_email.clear()
        client_email.send_keys("noris@mail.ru")

    def go_to_client_phone(self):
        client_phone = self.browser.find_element(*ProjectsPageLocators.PHONE_CLIENT)
        client_phone.clear()
        client_phone.send_keys("+972598706534")

    def go_to_save_new_client_btn(self):
        save_new_client_btn = self.browser.find_element(*ProjectsPageLocators.SAVE_CLIENT_BTN)
        save_new_client_btn.click()

    def go_to_client(self):
        client = self.browser.find_element(*ProjectsPageLocators.CLIENT)
        client.click()

    def go_to_delete_btn(self):
        delete_client_btn = self.browser.find_element(*ProjectsPageLocators.DELETE_CLIENT_BTN)
        delete_client_btn.click()

    def confirm_delete_btn(self):
        confirm_delete_client_btn = self.browser.find_element(*ProjectsPageLocators.CONFIRM_DELETE_CLIENT_BTN)
        confirm_delete_client_btn.click()
