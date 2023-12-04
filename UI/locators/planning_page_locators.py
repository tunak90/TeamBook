from selenium.webdriver.common.by import By


class PlanningPageLocators:
    USER_MENU = (By.ID, "openUserMenu")
    ADD_USER = (By.CLASS_NAME, "add-user-row__add-button")
    SELECT_USER_FIELD = (By.CSS_SELECTOR, "#add-user-dialog-popup > div.MuiDialog-container.MuiDialog-scrollPaper.css-"
                                          "ekeie0 > div > div.MuiDialogContent-root.css-1ty026z > div > div > div.tb-"
                                          "react-select-multi__value-container.tb-react-select-multi__value-container-"
                                          "-is-multi.css-1q92093")
    CREATE_NEW_USER = (By.CSS_SELECTOR, "#react-select-63-option-0")
