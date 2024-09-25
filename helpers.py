import requests
import allure
import random
import string
from data import *


@allure.step('Генерация строки с задаваемой длиной, состоящей из {length} букв нижнего регистра')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация данных из логина, пароля и имени для нового курьера')
def generate_random_payload():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


