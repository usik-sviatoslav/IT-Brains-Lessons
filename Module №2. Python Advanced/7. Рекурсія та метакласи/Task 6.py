
# Завдання №6. Напишіть рекурсивну функцію, яка підраховує глибину вкладеності списків.


def depth(lists):
    if len(lists) == 1:
        return 1
    return len(lists) - 1 + depth(lists.pop())


print(depth([1, [2, [3, [4, [5]]]]]))
