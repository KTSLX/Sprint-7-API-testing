import allure
from data import *
from helpers import *


class TestOrderList:

    @classmethod
    def setup_class(cls):
        courier = register_new_courier_and_return_login_password()
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        login_response = requests.post(LOGIN_URL, data=payload)
        cls.courier_id = login_response.json()["id"]

    @allure.title('Позитивная проверка получения списка заказов нового курьера по его courierId')
    @allure.description('Проверяется статус код и возвращение в теле ответа пустого списка заказов для нового курьера')
    def test_order_list_with_courier_id(self):
        response = requests.get(ORDER_ID_URL + str(self.courier_id))
        assert response.status_code == 200 and response.json()['orders'] == []

    @allure.title('Позитивная проверка получения общего списка заказов без указания courierId')
    @allure.description('Проверяется статус код и возвращение в теле ответа списка заказов')
    def test_order_list_without_courier_id(self):
        response = requests.get(ORDERS_URL)
        assert response.status_code == 200 and not len(response.json()['orders']) == 0


    @classmethod
    def teardown_class(cls):
        requests.delete(COURIER_URL + '/' + str(cls.courier_id), data={"id": f'{cls.courier_id}'})