from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REG_FIRST_NAME = (By.ID, "register-first-name")
    REG_LAST_NAME = (By.ID, "register-last-name")
    REG_BUSINESS_EMAIL = (By.ID, "register-email")
    REG_ORGANIZATION = (By.ID, "register-company-name")
    REG_PASSWORD = (By.ID, "password-field")
    REG_CHECKBOX = (By.CSS_SELECTOR, "div.register__right-side > div > div.register-privacy-policy-text > div > img")
    REG_CREATE_ORG_BTN = (By.ID, "create_org_btn")
    REG_SKIP = (By.CSS_SELECTOR, "body > div.MuiDialog-root.register-pop-up__container.MuiModal-root.css-126xj0f > "
                                 "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                 "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > p")
    REG_ERROR_MESSAGE = (By.CSS_SELECTOR, "div.register-form__inputs > div.form-error__error-message.undefined >"
                                          " div > p.form-error__error-text")

