from selenium.webdriver.common.by import By


class PlanningPageLocators:
    USER_MENU = (By.ID, "openUserMenu")
    ADD_USER = (By.CLASS_NAME, "add-user-row__add-button")
    SELECT_USER_FIELD = (By.CSS_SELECTOR, "#add-user-dialog-popup > div.MuiDialog-container.MuiDialog-scrollPaper.css-"
                                          "ekeie0 > div > div.MuiDialogContent-root.css-1ty026z > div > div > div.tb-"
                                          "react-select-multi__value-container.tb-react-select-multi__value-container-"
                                          "-is-multi.css-1q92093")
    CREATE_NEW_USER = (By.CSS_SELECTOR, "#react-select-63-option-0")
    TEAM_SELECT = (By.ID, "teamsSelect")
    NEW_TEAM = (By.ID, "newTeam")
    TEAM_NAME_FIELD = (By.ID, "teamName")
    CREATE_TEAM_BTN = (By.ID, "createTeamButton")
    CANCEL_TEAM_BTN = (By.CSS_SELECTOR, "div > div.MuiDialogContent-root.css-1ty026z > p > div.manage-team-dialog__"
                                        "team-row.creation > div:nth-child(2) > img:nth-child(2)")
    ROW_OF_TEAM = (By.CLASS_NAME, "manage-team-dialog__team-row")
    ERROR_MESSAGE_NAME = (By.CSS_SELECTOR, "div.MuiDialogContent-root.css-1ty026z > p > div.form-error__error-"
                                           "message.undefined > div > p.form-error__error-text")
