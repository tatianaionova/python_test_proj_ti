from tests.frontend.pages.home_page import HomePage
import allure

@allure.feature('Домашняя страница')
@allure.story('Проверка, что при нажатии на карту показывается корректное значение суммы')
def test_card_has_correct_amount(driver_chrome):
        home_page = HomePage(driver_chrome)
        home_page.open()
        all_card_amounts = home_page.find_all_card_amounts()
        assert len(all_card_amounts) == 6, "incorrect count of cards"

        for card in all_card_amounts:
            card.click()
            assert card.text == home_page.get_text_for_nominal_input(), "nominal is wrong for this card"
            assert home_page.is_button_active(card), "card is not active"