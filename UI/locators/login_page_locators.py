from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, ":r0:")
    LOGIN_PASSWORD = (By.ID, ":r1:")
    LINK_TO_REGISTRATION_PAGE = (By.CLASS_NAME, "login__input-side__login-link")
    LINK_TO_FORGOT_PASSWORD = (By.CLASS_NAME, "forgot-password")
    LOGIN_BTN = (By.ID, "login_btn")
    GOOGLE_LOGIN = (By.ID, "google_login_btn")
    AZURE_LOGIN = (By.ID, "azure_login_btn")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "div.login-form__inputs > div.form-error__error-message.undefined > "
                                            "div > p.form-error__error-text")
