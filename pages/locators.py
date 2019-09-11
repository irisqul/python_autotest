from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_IS_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main >.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")