from selenium.webdriver.common.by import By
from tests.frontend.pages.base_page import BasePage

class HomePage(BasePage):
    card_options_loc = (By.XPATH, "//button[starts-with(@class,'par-options__button')]")
    nominal_loc = (By.ID, "range-value-input")

    def find_all_card_amounts(self):
        return self.find_elements(*self.card_options_loc)

    def get_text_for_nominal_input(self):
        return self.find_element(*self.nominal_loc).get_attribute('value')

    def is_button_active(self, button):
        if "active" in button.get_attribute('class'):
            return True
        else:
            return False