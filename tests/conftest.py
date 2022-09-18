import pytest
from selenium.webdriver import Chrome

from tests.backend.api_client import ApiClient
from tests.config import BaseConfig

@pytest.fixture(scope='session')
def driver_chrome():
    driver = Chrome(BaseConfig.CHROME_EXECUTABLE_PATH)
    driver.implicitly_wait(BaseConfig.DEFAULT_TIMEOUT)
    driver.delay = BaseConfig.DEFAULT_TIMEOUT
    driver.max_delay = BaseConfig.MAX_TIMEOUT

    yield driver
    driver.quit()

@pytest.fixture()
def lenvendo_api():
    return ApiClient(base_url=BaseConfig.BASE_URL_API)