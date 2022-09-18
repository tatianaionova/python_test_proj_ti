import allure
from tests.backend.models.jstesttask import JsTestTask

@allure.feature('Поиск')
@allure.story('Проверка, что api вовзращает только правильные значения в порядке возврастания ')
def test_search_by_name_returns_correct_names(lenvendo_api):
    sort_field = 'name'
    search = 'Alcatel'
    url = f"js-test-task/?search={search}&sort_field={sort_field}"
    r = lenvendo_api.get(url)
    assert r.status_code == 200, f"response from server{r.status_code}"

    products = r.json()['products']

    listofproducts = [JsTestTask(product['name'], product['image'], product['price']) for product in products]
    for product in listofproducts:
        assert product['name'] != search, f"found wrong search param {product['name']}"

    sorted_products = sorted(products, key=lambda d: d['name'])
    assert sorted_products == products, "sorting is wrong"