
# Використовуючи API погоди, напишіть програму, яка запитує у користувача назву міста та повертає поточну
# температуру в цьому місті. Виведіть цю інформацію на екран.

import requests
import api_key


def get_weather(city, key):
    param = {"access_key": key.weather, "query": city}
    response = requests.get("http://api.weatherstack.com/current", param)
    api_response = response.json()

    location = api_response["location"]["name"]
    temperature = api_response["current"]["temperature"]

    print(f"Current temperature in {location} is {temperature}℃")


user_input = input("Enter a city name: ")
get_weather(user_input, api_key)
