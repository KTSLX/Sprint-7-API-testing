import pytest
import allure
from data import *
from helpers import *


class TestLoginCourier:
    @classmethod
    def setup_class(cls):
        cls.courier = register_new_courier_and_return_login_password()
        cls.payload = {
            "login": cls.courier[0],
            "password": cls.courier[1]
        }

    @allure.title('Позитивная проверка авторизации курьера с корректными данными')
    @allure.description('Проверяется статус код и возвращение id в теле ответа')
    def test_login_courier_true(self):
        r = requests.post(LOGIN_URL, data=self.payload)
        assert r.status_code == 200 and r.json()['id']

    payload_data = [["login", 504, LOGIN_EXPECTED_MESSAGE_504],
                    ["password", 400, LOGIN_EXPECTED_MESSAGE_400]]

    @allure.title('Проверка обязательных полей при авторизации курьера')
    @allure.description('Проверяется возвращение ошибки при отсутствии обязательного поля в запросе')
    @pytest.mark.parametrize('key, code, message', payload_data)
    def test_login_courier_without_required_field(self, key, code, message):
        payload = {key: self.payload[key]}
        r = requests.post(LOGIN_URL, data=payload)
        assert r.status_code == code and message in r.text

    @allure.title('Негативная проверка авторизации курьера с неверными параметрами')
    @allure.description('Проверяется возвращение ошибки при неверном логине или пароле')
    @pytest.mark.parametrize('key', ["login", "password"])
    def test_login_courier_with_incorrect_login_or_password(self, key):
        payload = {
            "login": self.courier[0],
            "password": self.courier[1]
        }
        payload[key] = payload[key][0:-1]
        r = requests.post(LOGIN_URL, data=payload)
        assert r.status_code == 404 and r.json()['message'] == LOGIN_EXPECTED_MESSAGE_404

    @allure.title('Негативная проверка авторизации курьера под несуществующим пользователем')
    @allure.description('Проверяется возвращение ошибки при несуществующем логине и пароле')
    def test_login_courier_non_existent_user(self):
        payload = generate_random_payload()
        r = requests.post(LOGIN_URL, data=payload)
        assert r.status_code == 404 and r.json()['message'] == LOGIN_EXPECTED_MESSAGE_404

    @classmethod
    def teardown_class(cls):
        login_response = requests.post(LOGIN_URL, data=cls.payload)
        courier_id = login_response.json()["id"]
        requests.delete(COURIER_URL + '/' + str(courier_id), data={"id": f'{courier_id}'})