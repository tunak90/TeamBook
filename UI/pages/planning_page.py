from UI.locators.planning_page_locators import PlanningPageLocators
from UI.pages.base_page import BasePage


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
