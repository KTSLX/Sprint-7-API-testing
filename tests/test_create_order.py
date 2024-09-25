import pytest
import allure
import requests
import json
from data import *
from helpers import *


class TestCreateOrder:

    @allure.title('Проверка создания заказа с выбором цвета самоката')
    @allure.description('Проверяется создание заказа с указанием разных вариантов цвета самоката')
    @pytest.mark.parametrize('color', SCOOTER_COLOR)
    def test_create_order_true(self, color):
        payload = ORDER_DATA
        payload["color"] = color
        r = requests.post(ORDERS_URL, data=json.dumps(payload))
        assert r.status_code == 201 and r.json()['track']