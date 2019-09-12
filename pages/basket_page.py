from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_login_url(self):
        assert BasketPageLocators.BASKET_URL in self.url, "Basket url is not presented"

    def should_be_empty_basket_message(self):
        basket_message = (self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)).text
        assert basket_message == BasketPageLocators.SHOULD_BE_BASKET_MESSAGE, f"Empty basket message '{basket_message}' is different from expected message '{BasketPageLocators.SHOULD_BE_BASKET_MESSAGE}'"

