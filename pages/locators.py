from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#login_link")

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

class BasketPageLocators():
    BASKET_URL = "basket"
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket - items: nth - of - type(1)")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    SHOULD_BE_BASKET_MESSAGE = "Your basket is empty."
