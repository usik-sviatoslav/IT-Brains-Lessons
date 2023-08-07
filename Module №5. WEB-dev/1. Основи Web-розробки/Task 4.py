
# Використовуючи API фотографій, розробіть програму, яка запитує у користувача ключове слово (наприклад, "кіт")
# та завантажує першу знайдену фотографію за цим ключовим словом. Збережіть фотографію на диск та відкрийте її
# за допомогою програми перегляду зображень на вашому комп'ютері.

import os
import re
import requests
import api_key


def get_image(key, img):
    url = f"https://www.googleapis.com/customsearch/v1?q={img}&cx={key.search_eng}&key={key.token}&searchType=image"
    response = requests.get(url)
    api_response = response.json()

    try:
        image_url = api_response["items"][0]["link"]
    except KeyError:
        return f'Не зміг знайти картинки по запиту "{img}"'

    try:
        name = api_response["spelling"]["correctedQuery"]
    except KeyError:
        name = img

    image = requests.get(image_url)
    filename = image_url.split(".")[-1]
    file_type = re.findall(r"^\w+", filename).pop()

    save_path = os.path.join("C:\\Users\\Usik Sviatoslav\\Downloads\\Internet", f"{name}.{file_type}")
    with open(save_path, "wb") as file:
        file.write(image.content)
    return f"Зображення збережено у {save_path}."


while True:
    user_input = input("Введи яку картинку ти хочеш отримати: ")
    print(get_image(api_key, user_input))
    print()
