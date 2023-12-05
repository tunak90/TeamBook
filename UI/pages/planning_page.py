import data
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.pages.base_page import BasePage
import uuid


class PlanningPage(BasePage):
    def go_to_add_user(self):
        add_user = self.browser.find_element(*PlanningPageLocators.ADD_USER)
        add_user.click()

    def go_to_select_user_field(self):
        select_user_field = self.browser.find_element(*PlanningPageLocators.SELECT_USER_FIELD)
        select_user_field.click()

    def go_to_create_new_user(self):
        create_new_user = self.browser.find_element(*PlanningPageLocators.CREATE_NEW_USER)
        create_new_user.click()

    def go_to_team_select(self):
        team_select = self.browser.find_element(*PlanningPageLocators.TEAM_SELECT)
        team_select.click()

    def go_to_new_team(self):
        new_team = self.browser.find_element(*PlanningPageLocators.NEW_TEAM)
        new_team.click()

    def go_to_team_name_field(self):
        team_name_field = self.browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        e = str(uuid.uuid4().clock_seq)
        team_name_field.send_keys(data.valid_name_of_team + e)

    def go_to_create_team_btn(self):
        create_team_btn = self.browser.find_element(*PlanningPageLocators.CREATE_TEAM_BTN)
        create_team_btn.click()

    def go_to_cancel_team_btn(self):
        cancel_team_btn = self.browser.find_element(*PlanningPageLocators.CANCEL_TEAM_BTN)
        cancel_team_btn.click()
