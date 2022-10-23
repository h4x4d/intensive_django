import allure
from hamcrest import assert_that, equal_to


@allure.title('Testing nonexistent page')
def test_homepage_get(client):
    with allure.step('Getting /abracadabra'):
        response = client.get('/abracadabra')
    with allure.step('Asserting status'):
        assert_that(response.status_code, equal_to(404),
                    f'Expected code was 404, but got {response.status_code}')
