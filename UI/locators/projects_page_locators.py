from selenium.webdriver.common.by import By


class ProjectsPageLocators:
    CREATE_PROJECT = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]/p[1]/div[1]")
    NAME = (By.ID, "projectName")
    SHORT_NAME = (By.ID, "projectShortName")
    CLIENT_DROP_DOWN_LIST = (By.XPATH, "//*[@id='tags-outlined']/div[1]/div[1]")
    SALVOR_CLIENT = (By.XPATH, "//div[@id='react-select-3-option-1']")
    ANALYTICS_DROP_DOWN_LIST = (By.XPATH, "//*[@id='selectBillable']/div[1]/div[1]")
    BILLABLE = (By.XPATH, "//div[@id='react-select-4-option-0']")
    ESTIMATED_HOURS = (By.ID, "estimated")
    MANAGER_DROP_DOWN_LIST = (By.XPATH, "//div[3]/div[2]/p[2]/div/div/div")
    PERSON = (By.CSS_SELECTOR, "#react-select-5-option-2")
    STATUS_DROP_DOWN_LIST = (By.XPATH, "//div[4]/div/p[2]/div/div/div")
    TO_BE_CONFIRMED = (By.CSS_SELECTOR, "#react-select-6-option-1")
    START_DATE_CHECKBOX = (By.CSS_SELECTOR, ".project-form__field:nth-child(1) > .tb-checkbox")
    # CLICK_ON_CALENDAR = (By.CSS_SELECTOR, ".MuiInput-input")
    CLICK_ON_CALENDAR = (By.XPATH, "//p[2]/div/div/input")
    CHOOSE_DATE = (By.CSS_SELECTOR, ".MuiPickersCalendar-week:nth-child(2) > div:nth-child(5) .MuiTypography-root")
    END_DATE_CHECKBOX = (By.CSS_SELECTOR, ".project-form__field:nth-child(2) > .tb-checkbox")
    CREATE_BTN = (By.XPATH, "//button[@id='createProject']/p")
    PROJECT_SUCCESS_MESSAGE = (By.XPATH, "//*[@id='root']/div[2]/div[2]/p[1]")

    PROJECT = (By.XPATH, "//p[contains(.,'Dental Clinic')]")
    EDIT_PROJECT_BTN = (By.XPATH, "//p[contains(.,'Edit Project')]")
    ESTIMATED_HOURS_EDIT = (By.ID, "estimated")
    SAVE_BTN = (By.XPATH, "//*[@id='updateProject']/p[1]")

    ARCHIVE_BTN = (By.XPATH, "//*[@id='deleteProjectFormButton']")
    CONFIRM_ARCHIVE_BTN = (By.XPATH, "//p[contains(.,'Archive')]")
    ARCHIVE_DROP_DOWN_LIST = (By.XPATH, "//div[@id='root']/div[2]/div/div[2]/div/div[2]/div/div/div/div")
    CHOOSE_ARCHIVED = (By.ID, "react-select-2-option-1")
    CHECK_BOX = (By.XPATH, "//*[@id='root']/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/img[1]")
    DELETE_BTN = (By.ID, "deleteProjectFormButton")
    CONFIRM_DELETE_BTN = (By.XPATH, "//p[contains(.,'Delete')]")
    PROJECT_LIST = (By.CSS_SELECTOR, ".project-list__block")
    PROJECT_ERROR_MESSAGE = (By.CSS_SELECTOR, ".form-error__main-text")

    MANAGE_CLIENTS = (By.CSS_SELECTOR, ".filter-row__button-caption > p")
    NEW_CLIENT = (By.ID, "createClient")
    NAME_CLIENT = (By.CSS_SELECTOR, "input:nth-child(1)")
    EMAIL_CLIENT = (By.CSS_SELECTOR, ".clients-modal__row > input:nth-child(2)")
    PHONE_CLIENT = (By.CSS_SELECTOR, ".clients-modal__row > input:nth-child(3)")
    SAVE_CLIENT_BTN = (By.XPATH, "//img[@alt='check']")
    DELETE_CLIENT_BTN = (By.XPATH, "(//img[@alt='trash'])[2]")
    CONFIRM_DELETE_CLIENT_BTN = (By.XPATH, "//p[contains(.,'Delete')]")
    EDIT_CLIENT = (By.XPATH, "(//img[@alt='pencil'])[2]")
    CLIENT = (By.XPATH, "//p[contains(.,'Noris')]")





