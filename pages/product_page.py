from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_text(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_text(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def should_be_correct_success_message(self, expected_name):
        actual_name = self.get_success_message_text()
        assert expected_name == actual_name, f"Expected '{expected_name}' but got '{actual_name}'"

    def should_be_correct_basket_total(self, expected_price):
        actual_price = self.get_basket_total_text()
        assert expected_price == actual_price, f"Expected '{expected_price}' but got '{actual_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"