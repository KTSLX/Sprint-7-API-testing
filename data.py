MAIN_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
COURIER_URL = MAIN_URL + '/courier'
LOGIN_URL = COURIER_URL + '/login'
ORDERS_URL = MAIN_URL + '/orders'
ORDER_ID_URL = ORDERS_URL + '?courierId='

CREATE_EXPECTED_MESSAGE_201 = '{"ok":true}'
CREATE_EXPECTED_MESSAGE_400 = 'Недостаточно данных для создания учетной записи'
CREATE_EXPECTED_MESSAGE_409 = 'Этот логин уже используется. Попробуйте другой.'
LOGIN_EXPECTED_MESSAGE_400 = 'Недостаточно данных для входа'
LOGIN_EXPECTED_MESSAGE_404 = 'Учетная запись не найдена'
LOGIN_EXPECTED_MESSAGE_504 = 'Service unavailable'

ORDER_DATA = {
    "firstName": "Алексан",
    "lastName": "Куцовый",
    "address": "ГрафствоКуц",
    "metroStation": 5,
    "phone": "+79788327459",
    "rentTime": 4,
    "deliveryDate": "2027-07-30",
    "comment": "домофон 666",
}

SCOOTER_COLOR = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]