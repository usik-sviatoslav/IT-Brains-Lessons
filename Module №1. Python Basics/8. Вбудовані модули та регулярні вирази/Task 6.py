
# Завдання №6. Напишіть регулярний вираз, який перевіряє, чи містить рядок дату у форматі "день-місяць-рік".

import re

txt = 'Наприклад: “05-06-2023” - валідний. “05.06.2023” - не валідний'
result = re.search(r"\d{2}-\d{2}-\d{4}", txt)
print(result)
