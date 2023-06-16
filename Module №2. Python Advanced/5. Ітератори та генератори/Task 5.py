
# Завдання №5. Реалізуйте ітератор для перебору всіх ключів словника.

users_dict = {
    "id0001": "John", "id0002": "Emma", "id0003": "Daniel", "id0004": "Sophia", "id0005": "Michael",
    "id0006": "Olivia", "id0007": "Matthew", "id0008": "Ava", "id0009": "William", "id0010": "Isabella"
}


class Iterator:
    def __init__(self, users):
        self.users = users

    def __iter__(self):
        self.current_user = 0
        return self

    def __next__(self):
        if self.current_user >= len(self.users):
            raise StopIteration
        keys = list(self.users.keys())
        current_key = keys[self.current_user]
        current_value = self.users[current_key]
        self.current_user += 1
        return current_key, current_value


for key, value in Iterator(users_dict):
    print(f"{key}: {value}")
