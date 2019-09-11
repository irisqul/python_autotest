from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IS_ADDED_MESSAGE), "There is no success message after product has been added"

    def product_name_and_added_product_name_are_the_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, f"Product name '{product_name}' and added product name '{added_product_name}' are not the same"

    def product_price_and_added_product_price_are_the_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"Product price '{ProductPageLocators.PRODUCT_PRICE}' and basket price '{ProductPageLocators.BASKET_PRICE}' are not the same"
