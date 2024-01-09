from selenium.webdriver.common.by import By


class ProfilePageLocators:
    SECTION_GENERAL_INFO = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]")
    EDIT_BUTTON = (By.ID, "update")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    PHONE_NUMBER = (By.ID, "phone-number")
    YOUR_TIME_ZONE = (By.XPATH, "//*[@id='time-zone']/div[1]/div[1]")
    CHOOSE_YOUR_TIME_ZONE = (By.XPATH, "//div[@id='react-select-2-option-35']")
    CHOOSE_LANGUAGE = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[5]/div[1]/img[1]")

    # ADD_PHOTO = (By.CSS_SELECTOR, "div:nth-child(1) > span")
    ADD_PHOTO = (By.CSS_SELECTOR, "div#root > div:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(2) > "
                                   "div > div > div > div > div > div > div")
    SET_AS_PROFILE_PHOTO_BTN = (By.XPATH, "//*[@id='save-notifications-changes']/p[1]")
    SAVE_BUTTON_GENERAL_INFO = (By.ID, "save-changes")
    PROFIlE_SUCCESS_MESSAGE = (By.XPATH, "//*[@id='root']/div[2]/div[2]/p[1]")
    PROFILE_ERROR_MESSAGE = (By.CSS_SELECTOR, ".form-error__main-text")

    SECTION_EMAIL_AND_PASSWORD = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/p[1]")
    NEW_EMAIL = (By.ID, "newEmail")
    SAVE_BUTTON_NEW_EMAIL = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/p[1]")
    CURRENT_PASSWORD = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > "
                                         "div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                         "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                         "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
    NEW_PASSWORD = (By.XPATH, "//input[@id=':rb:']")
    CONFIRM_NEW_PASSWORD = (By.XPATH, "//input[@id=':rd:']")
    SAVE_BUTTON_NEW_PASSWORD = (By.XPATH, "//div[2]/button/p")
    PROFIlE_SUCCESS_MESSAGE3 = (By.XPATH, "//*[@id='root']/div[2]/div[2]/p[1]")

    SECTION_SCHEDULE = (By.XPATH, "//p[contains(.,'Schedule')]")
    SATURDAY_CHECKBOX = (By.CSS_SELECTOR, "div:nth-child(6) > img")
    SAVE_BUTTON_SCHEDULE = (By.XPATH, "//p[contains(.,'Save')]")
    PROFIlE_SUCCESS_MESSAGE4 = (By.XPATH, "//*[@id='root']/div[2]/div[2]/p[1]")

    SECTION_NOTIFICATIONS = (By.XPATH, "//p[contains(.,'Notifications')]")
    OPERATIONAL_PLANNING_CHECKBOX = (By.CSS_SELECTOR, ".notifications-group:nth-child(1) > .notifications-select-row "
                                                      "> img")
    DAILY_NOTIFICATIONS = (By.CSS_SELECTOR, ".notifications-block:nth-child(2) .tb-radio-button")
    IMMEDIATE_NOTIFICATIONS = (By.CSS_SELECTOR, ".notifications-block:nth-child(3) .tb-radio-button")
    CAPACITY_PLANNING_CHECKBOX = (By.CSS_SELECTOR, ".notifications-group:nth-child(2) img")
    ARROW_UP = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/img[1]")
    ACTUAL_TIME_TRACKING = (By.CSS_SELECTOR, ".notifications-group:nth-child(3) img")
    ARROW_DOWN = (By.CSS_SELECTOR, ".notifications-group:nth-child(3) img:nth-child(2)")
    SAVE_BUTTON_NOTIFICATIONS = (By.XPATH, "//*[@id='save-notifications-changes']/p[1]")
    PROFIlE_SUCCESS_MESSAGE2 = (By.XPATH, "//*[@id='root']/div[2]/div[2]/p[1]")

