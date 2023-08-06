
# Використовуючи API фотографій, розробіть програму, яка запитує у користувача ключове слово (наприклад, "кіт")
# та завантажує першу знайдену фотографію за цим ключовим словом. Збережіть фотографію на диск та відкрийте її
# за допомогою програми перегляду зображень на вашому комп'ютері.

import os
import requests
import api_key


def get_image(key, img):
    response = requests.get(f"https://api.pexels.com/v1/search?query={img}", headers={"Authorization": key.image})
    api_response = response.json()

    if len(api_response["photos"]) != 0:
        image_url = api_response["photos"][0]["src"]["large2x"]
        image_name = api_response["photos"][0]["alt"]
        image = requests.get(image_url)

        save_path = os.path.join("C:\\Users\\Usik Sviatoslav\\Downloads\\Internet", f"{image_name}.jpg")
        with open(save_path, 'wb') as file:
            file.write(image.content)
        print(f'Зображення збережено у {save_path}.')
    else:
        print("По вашому запиту нічого не знайдено")


while True:
    user_input = input("Введи яку картинку ти хочеш отримати: ")
    get_image(api_key, user_input)
    print()
