import requests
import allure
from data import *
from helpers import *


@allure.step('Регистрация нового курьера и получение списка из его логина, пароля и имени')
def register_new_courier_and_return_login_password():
    login_pass = []
    payload = generate_random_payload()
    response = requests.post(COURIER_URL, data=payload)
    if response.status_code == 201:
        login_pass.append(payload["login"])
        login_pass.append(payload["password"])
        login_pass.append(payload["firstName"])
    return login_pass