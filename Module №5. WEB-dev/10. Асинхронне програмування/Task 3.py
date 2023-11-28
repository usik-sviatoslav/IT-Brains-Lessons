"""
Завдання №3. Асинхронність: Асинхронний Web-скрейпінг

Створити асинхронний Python скрипт, який здійснює скрейпінг вебсайтів для пошуку конкретного ключового слова на них.
Скрипт повинен одночасно звертатися до декількох вебсайтів.

Вимоги:
1. Скрипт повинен приймати список URL і ключове слово для пошуку.
2. Скрипт повинен асинхронно завантажувати вміст кожної вебсторінки та шукати на ній задане ключове слово.
3. Результат (знайдено/не знайдено) повинен виводитись на екран для кожного URL.

*У вас у цій задачі може виникнути помилка з SSL-сертифікатом, і в конспекті ми розбирали що робити в такому випадку.

"""
import asyncio
import re
import time

import aiohttp
from bs4 import BeautifulSoup


async def match_count(url, match_word):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_content = await response.text()
            soup = BeautifulSoup(html_content, 'lxml')

            find_word = soup.find_all(
                ['title', 'div', 'span', 'p', 'a'],
                string=re.compile(f'{match_word.capitalize()} | {match_word.lower()} | {match_word.upper()}')
            )

            print(f'На сайті {url} знайдено {len(find_word)} слова "{match_word}"')


async def task():
    urls = [
        ('https://www.python.org/', 'python'),
        ('https://www.djangoproject.com/', 'django'),
        ('https://docs.docker.com/', 'docker'),
    ]

    tasks = [match_count(url, match_word) for url, match_word in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(task())
    print("Загальний час: ", time.time() - start_time, "сек")
