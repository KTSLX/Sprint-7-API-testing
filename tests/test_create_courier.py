import pytest
import allure
import requests
from data import *
from helpers import *


class TestCreateCourier:

    @allure.title('Позитивная проверка создания курьера с корректными данными')
    @allure.description('Проверяется статус код и тело ответа')
    def test_create_courier_true(self):
        payload = generate_random_payload()
        r = requests.post(COURIER_URL, data=payload)
        assert r.status_code == 201 and r.text == CREATE_EXPECTED_MESSAGE_201

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    @allure.description('Проверяется возвращение ошибки при создании курьера с существующим логином и паролем')
    def test_create_courier_once(self):
        payload = generate_random_payload()
        requests.post(COURIER_URL, data=payload)
        r = requests.post(COURIER_URL, data=payload)
        assert r.status_code == 409 and r.json()['message'] == CREATE_EXPECTED_MESSAGE_409

    @allure.title('Проверка обязательных полей при создании курьера')
    @allure.description('Проверяется возвращение ошибки при отсутствии обязательного поля в запросе')
    @pytest.mark.parametrize('required_field', ["login", "password"])
    def test_create_courier_without_required_field(self, required_field):
        payload = generate_random_payload()
        del payload[required_field]
        r = requests.post(COURIER_URL, data=payload)
        assert r.status_code == 400 and r.json()['message'] == CREATE_EXPECTED_MESSAGE_400