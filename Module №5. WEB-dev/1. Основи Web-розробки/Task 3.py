
# Використовуючи API курсів валют, розробіть програму, яка запитує у користувача вихідну валюту, потрібну
# валюту та суму, і обчислює конвертацію з однієї валюти в іншу. Виведіть отриманий результат на екран.

import requests
import api_key


def get_exchange(key, symbol_1, symbol_2, amount):
    param = {"access_key": key.exchange, "base": symbol_1, "symbols": symbol_2}
    response = requests.get("http://api.exchangeratesapi.io/v1/latest", param)
    api_response = response.json()

    result = amount * api_response["rates"][symbol_2]
    print(f"{amount:_} {symbol_1} = {round(result, 2):_} {symbol_2}".replace("_", " "))


get_exchange(api_key, "EUR", "UAH", 12345)
