
# Напишіть функцію, яка отримує URL API та повертає відповідь з нього в форматі JSON. Виведіть цю відповідь на екран.

import requests
import api_key as key

my_headers = {
    "Authorization": key.skillzrun,
    "Company-Id": "-1",
    "Content-Type": "application/json",
    "Device": "Browser/WebApp/1/0.0.1/1.0.11",
    "Timezoneoffset": "10800000"
}
my_url = "https://skillzrun.com/api/v1/branchesTree"


def get_url(url, headers):
    response = requests.get(url, headers=headers)
    result = response.json()
    return result


print(get_url(my_url, my_headers))
