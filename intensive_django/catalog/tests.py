import allure
import pytest
from hamcrest import assert_that, equal_to


@allure.title('Testing catalog page')
def test_catalog_get(client):
    with allure.step('Getting catalog page'):
        response = client.get('/catalog/')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(200),
                    f'Expected code was 200, but got {response.status_code}')


@pytest.mark.parametrize("page_to_go,expected_status_code",
                         [("1", 200), ("1598", 200), ("a", 404),
                          ("0", 404), ("-11", 404), ])
@allure.title('Testing catalog direct pages')
def test_catalog_direct_get(client, page_to_go, expected_status_code):
    with allure.step('Getting catalog page'):
        response = client.get(f'/catalog/{page_to_go}')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(expected_status_code),
                    f'Expected code was {expected_status_code}, '
                    f'but got {response.status_code}')
